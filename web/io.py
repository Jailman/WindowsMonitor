#!C:\Python27\python.exe
# coding=utf-8

import time
import socket
import psutil
import sqlite3
import threading

host = socket.gethostname()

class dioThread (threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        diskio_mon()


def diskio_mon():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    while True:
        dio_data = {}
        dio_data['Host'] = host
        dio_data['Time'] = int(int(time.time()) + 8 * 3600)
        read_start_count = psutil.disk_io_counters()[0]
        write_start_count = psutil.disk_io_counters()[1]
        read_start_byte = psutil.disk_io_counters()[2]
        write_start_byte = psutil.disk_io_counters()[3]
        time.sleep(1)
        read_end_count = psutil.disk_io_counters()[0]
        write_end_count = psutil.disk_io_counters()[1]
        read_end_byte = psutil.disk_io_counters()[2]
        write_end_byte = psutil.disk_io_counters()[3]
        dio_data["Read_speed_count"] = int(read_end_count - read_start_count)
        dio_data["Write_speed_count"] = int(write_end_count - write_start_count)
        dio_data["Read_speed_kb"] = int(read_end_byte - read_start_byte)
        dio_data["Write_speed_kb"] = int(write_end_byte - write_start_byte)
        dio_data["Read_time"] = int(psutil.disk_io_counters()[4])
        dio_data["Write_time"] = int(psutil.disk_io_counters()[5])
        print dio_data
        try:
            sql = "INSERT INTO `diskio_stat` (`host`, `read_speed_count`, `write_speed_count`, `read_speed_kb`, `write_speed_kb`, `read_time`, `write_time`, `time`) VALUES('%s', '%d', '%d', '%d', '%d', '%d', '%d', '%d')" % (
                dio_data['Host'], dio_data["Read_speed_count"], dio_data["Write_speed_count"], dio_data["Read_speed_kb"], dio_data["Write_speed_kb"], dio_data["Read_time"], dio_data["Write_time"], int(dio_data['Time']))
            cur.execute(sql)
            cx.commit()
        except:
            pass
        print "Diskio DB insert OK"
        time.sleep(5)

if __name__ == "__main__":
    dioThread = dioThread()
    dioThread.start()
