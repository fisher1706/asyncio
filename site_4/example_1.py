#!/usr/bin/python

import os
import errno
import signal
import select
import socket
import logging
import time

logger = logging.getLogger('main')

BIND_ADDRESS = ('localhost', 8999)
BACKLOG = 5


class Handler:
    def __init__(self, sock, clinet_ip, client_port):
        self.log('Start to process request from %s:%d' % (clinet_ip, client_port))
        self.sock = sock
        self.ready_to_read = True
        self.ready_to_write = False
        self.i_am_done = False
        self.in_buffer = b''
        self.out_buffer = b''
        self.wait_until = 1e10 # недостижимое время

    def log(self, message):
        logger.info('[id=%d] %s' % (id(self), message))

    def get_data_from_socket(self):
        while True:
            chank = self.sock.recv(1024)
            self.in_buffer += chank
            if len(chank) < 1024:
                break
        if self.in_buffer.endswith(b'\n'):
            self.log('In buffer collected: ' + repr(self.in_buffer))
            self.ready_to_read = False
            # ждём 5 секунд (изображаем обращение к внешнему процессу)
            self.wait_until = time.time() + 5

    def time_tick(self):
        if time.time() < self.wait_until:
            return
        # получаем результат
        try:
            result = str(eval(self.in_buffer, {}, {}))
        except Exception as e:
            result = repr(e)
        self.out_buffer = result.encode('utf-8') + b'\r\n'
        self.log('Out buffer ready: ' + repr(self.out_buffer))
        # выставляем флаг, что мы готовы отдавать результат
        self.ready_to_write = True

    def write_data_to_socket(self):
        n = self.sock.send(self.out_buffer)
        if n == len(self.out_buffer):
            # все отправлено
            self.log('Done.')
            self.i_am_done = True
            self.ready_to_write = False
            self.sock.close()
        else:
            # удаляем часть буфера, которая уже отправлена
            self.out_buffer = self.out_buffer[n:]


class Listener:
    def __init__(self, sock):
        self.ready_to_read = True
        self.ready_to_write = False
        self.i_am_done = False

    def time_tick(self):
        pass # затычка для совместимости

# глобальная карта соответствия fileno <-> объект_обработчик
socket_map = {}

def server_forever():
    # создаём слушающий сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # re-use port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(BIND_ADDRESS)
    sock.listen(BACKLOG)
    # слушаем и при получении нового входящего соединения,
    # порождаем объект Handler, который будет его обрабатывать
    logger.info('Listning no %s:%d...' % BIND_ADDRESS)
    # добавляем наш слушающий сокет в карту
    # обернув его в Listner для обеспечения единого интерфейса
    # всех объектов-контекстов
    socket_map[sock.fileno()] = Listener(sock)
    while True:
        # собираем все сокеты, для которых
        # есть операции, ожидающие чтения или записи
        to_read = []
        to_write = []
        for fileno, obj in socket_map.items():
            obj.time_tick()
            if obj.ready_to_read:
                to_read.append(fileno)
            if obj.ready_to_write:
                to_write.append(fileno)
        # проверяем фактическое состояние сокета и его
        # готовность к вводу-выводу
        has_data_to_read, waiting_for_writing, errors = select.select(to_read, to_write, [], 1)
        # обрабатываем все чтения
        for fileno in has_data_to_read:
            obj = socket_map[fileno]
            # проверяем тип сокета
            if type(obj) is Listener:
                # мы получили новое входящее соединение
                try:
                    connection, (client_ip, clinet_port) = sock.accept()
                except IOError as e:
                    if e.errno == errno.EINTR:
                        continue
                    raise
                # не блокирующий
                connection.setblocking(0)
                # cоздаём новый объект для асинхронного
                # обслуживания соединения
                socket_map[connection.fileno()] = Handler(connection, client_ip, clinet_port)
            else:
                # мы получили данные
                obj.get_data_from_socket()
        # обрабатываем все записи (тут всё просто, альтернатив нет)
        for fileno in waiting_for_writing:
            socket_map[fileno].write_data_to_socket()
        # удаляем все обработчики, которые завершили свою работу
        to_delete = []
        for fileno, obj in socket_map.items():
            if obj.i_am_done:
                to_delete.append(fileno)
        for fileno in to_delete:
            del socket_map[fileno]


def main():
    # настраиваем логгинг
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', '%H:%M:%S')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.info('Run')
    # запускаем сервер
    server_forever()


if __name__ == '__main__':
    main()





















