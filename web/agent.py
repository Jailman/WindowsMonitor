#!C:\Python27\python.exe
# coding=utf-8

import time
import socket
import psutil
import sqlite3
import threading

# cx = sqlite3.connect("falcon.db")
# cur = cx.cursor()
host = socket.gethostname()


class cpuThread (threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        cpu_mon()


class memThread (threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        mem_mon()


class dcThread (threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        diskc_mon()


class dioThread (threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        diskio_mon()


class nioThread (threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        nicio_mon()


def cpu_mon():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    while True:
        cpu_data = {}
        cpu_data['Host'] = host
        cpu_data['Time'] = int(int(time.time()) + 8 * 3600)
        cpu_data['CPUpercent'] = int(psutil.cpu_percent())
        cpu_data['CPUuser'] = int(psutil.cpu_times()[0])
        cpu_data['CPUsystem'] = int(psutil.cpu_times()[1])
        cpu_data['CPUidle'] = int(psutil.cpu_times()[2])
        print cpu_data
        try:
            sql = "INSERT INTO `cpu_stat` (`host`,`cpu_percent`,`cpu_user`,`cpu_system`, `cpu_idle`, `time`) VALUES('%s', '%d', '%d', '%d', '%d', '%d')" % (
                cpu_data['Host'], cpu_data['CPUpercent'], cpu_data['CPUuser'], cpu_data['CPUsystem'], cpu_data['CPUidle'], int(cpu_data['Time']))
            cur.execute(sql)
            cx.commit()
        except:
            pass
        print "CPU DB insert OK"
        time.sleep(10)


def mem_mon():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    while True:
        mem_data = {}
        mem_data['Host'] = host
        mem_data['Time'] = int(int(time.time()) + 8 * 3600)
        mem_data['MemTotal'] = int(psutil.virtual_memory()[0]) / 1024 / 1024
        mem_data['MemUsage'] = int(psutil.virtual_memory()[3]) / 1024 / 1024
        mem_data['MemFree'] = int(psutil.virtual_memory()[1]) / 1024 / 1024
        print mem_data
        try:
            sql = "INSERT INTO `mem_stat` (`host`,`mem_free`,`mem_usage`,`mem_total`,`time`) VALUES('%s', '%d', '%d', '%d', '%d')" % (
                mem_data['Host'], mem_data['MemFree'], mem_data['MemUsage'], mem_data['MemTotal'], int(mem_data['Time']))
            cur.execute(sql)
            cx.commit()
        except:
            pass
        print "RAM DB insert OK"
        time.sleep(10)


def diskc_mon():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    while True:
        dc_data = {}
        dc_data['Host'] = host
        dc_data['Time'] = int(int(time.time()) + 8 * 3600)
        dc_data['DCtotal'] = int(psutil.disk_usage("C:")[0]) / 1024 / 1024
        dc_data['DCused'] = int(psutil.disk_usage("C:")[1]) / 1024 / 1024
        dc_data['DCfree'] = int(psutil.disk_usage("C:")[2]) / 1024 / 1024
        dc_data['DCpercent'] = int(psutil.disk_usage("C:")[3])
        print dc_data
        try:
            sql = "INSERT INTO `diskc_stat` (`host`,`disk_total`,`disk_used`,`disk_free`, `disk_percent`,`time`) VALUES('%s', '%d', '%d', '%d', '%d', '%d')" % (
                dc_data['Host'], dc_data['DCtotal'], dc_data['DCused'], dc_data['DCfree'], dc_data['DCpercent'], int(dc_data['Time']))
            cur.execute(sql)
            cx.commit()
        except:
            pass
        print "DiskC DB insert OK"
        time.sleep(10)


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
        dio_data["Write_speed_count"] = int(
            write_end_count - write_start_count)
        dio_data["Read_speed_kb"] = int(read_end_byte - read_start_byte) / 1024
        dio_data["Write_speed_kb"] = int(write_end_byte - write_start_byte) / 1024
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


def nicio_mon():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    while True:
        nio_data = {}
        nio_data['Host'] = host
        nio_data['Time'] = int(int(time.time()) + 8 * 3600)
        sent_start_byte = psutil.net_io_counters()[0]
        recv_start_byte = psutil.net_io_counters()[1]
        sent_start_pkt = psutil.net_io_counters()[2]
        recv_start_pkt = psutil.net_io_counters()[3]
        time.sleep(1)
        sent_end_byte = psutil.net_io_counters()[0]
        recv_end_byte = psutil.net_io_counters()[1]
        sent_end_pkt = psutil.net_io_counters()[2]
        recv_end_pkt = psutil.net_io_counters()[3]
        nio_data["Sent_speed_kb"] = int(sent_end_byte - sent_start_byte) / 1024
        nio_data["Recv_speed_kb"] = int(recv_end_byte - recv_start_byte) / 1024
        nio_data["Sent_speed_pkt"] = int(sent_end_pkt - sent_start_pkt)
        nio_data["Recv_speed_pkt"] = int(recv_end_pkt - recv_start_pkt)
        print nio_data
        try:
            sql = "INSERT INTO `nicio_stat` (`host`, `sent_speed_kb`, `recv_speed_kb`, `sent_speed_pkt`, `recv_speed_pkt`, `time`) VALUES('%s', '%d', '%d', '%d', '%d', '%d')" % (
                nio_data['Host'], nio_data["Sent_speed_kb"], nio_data["Recv_speed_kb"], nio_data["Sent_speed_pkt"], nio_data["Recv_speed_pkt"], int(nio_data['Time']))
            cur.execute(sql)
            cx.commit()
        except:
            pass
        print "Nicio DB insert OK"
        time.sleep(5)


if __name__ == "__main__":
    cputhread = cpuThread()
    memthread = memThread()
    dcThread = dcThread()
    dioThread = dioThread()
    nioThread = nioThread()
    cputhread.start()
    memthread.start()
    dcThread.start()
    dioThread.start()
    nioThread.start()
