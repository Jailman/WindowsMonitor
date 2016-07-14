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


if __name__ == "__main__":
    cputhread = cpuThread()
    memthread = memThread()
    dcThread = dcThread()
    cputhread.start()
    memthread.start()
    dcThread.start()
