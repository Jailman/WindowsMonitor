#!C:\Python27\python.exe
# coding=utf-8

import inspect
import time
import urllib
import urllib2
import json
import socket
import psutil
import sqlite3

cx = sqlite3.connect("falcon.db")
cur = cx.cursor()


class cpu_mon:

    def __init__(self):
        self.data = {}

    def getTime(self):
        return str(int(time.time()) + 8 * 3600)

    def getHost(self):
        return socket.gethostname()

    def getCPUpercent(self):
        percent = psutil.cpu_percent()
        return int(percent)

    def getCPUuser(self, noBufferCache=True):
        user = psutil.cpu_times()[0]
        return int(user)

    def getCPUsystem(self, noBufferCache=True):
        system = psutil.cpu_times()[1]
        return int(system)

    def getCPUidle(self, noBufferCache=True):
        idle = psutil.cpu_times()[2]
        return int(idle)

    def runAllGet(self):
        # 自动获取mon类里的所有getXXX方法，用XXX作为key，getXXX()的返回值作为value，构造字典
        for fun in inspect.getmembers(self, predicate=inspect.ismethod):
            if fun[0][:3] == 'get':
                self.data[fun[0][3:]] = fun[1]()
        return self.data


class mem_mon:

    def __init__(self):
        self.data = {}

    def getTime(self):
        return str(int(time.time()) + 8 * 3600)

    def getHost(self):
        return socket.gethostname()

    # def getLoadAvg(self):
    #     with open('/proc/loadavg') as load_open:
    #         a = load_open.read().split()[:3]
    #         return ','.join(a)

    def getMemTotal(self):
        total = psutil.virtual_memory()[0]
        return int(total / 1024 / 1024)

    def getMemUsage(self, noBufferCache=True):
        used = psutil.virtual_memory()[3]
        return int(used / 1024 / 1024)

    def getMemFree(self, noBufferCache=True):
        free = psutil.virtual_memory()[1]
        return int(free / 1024 / 1024)

    def runAllGet(self):
        # 自动获取mon类里的所有getXXX方法，用XXX作为key，getXXX()的返回值作为value，构造字典
        for fun in inspect.getmembers(self, predicate=inspect.ismethod):
            if fun[0][:3] == 'get':
                self.data[fun[0][3:]] = fun[1]()
        return self.data


if __name__ == "__main__":
    while True:
        c = cpu_mon()
        cpu_data = c.runAllGet()
        print cpu_data
        try:
            cpu_sql = "INSERT INTO `cpu_stat` (`host`,`cpu_percent`,`cpu_user`,`cpu_system`, `cpu_idle`, `time`) VALUES('%s', '%d', '%d', '%d', '%d', '%d')" % (
                cpu_data['Host'], cpu_data['CPUpercent'], cpu_data['CPUuser'], cpu_data['CPUsystem'], cpu_data['CPUidle'], int(cpu_data['Time']))
            cur.execute(cpu_sql)
            cx.commit()
        except:
            pass
        print "CPU DB insert OK"
        m = mem_mon()
        mem_data = m.runAllGet()
        print mem_data
        try:
            mem_sql = "INSERT INTO `mem_stat` (`host`,`mem_free`,`mem_usage`,`mem_total`,`time`) VALUES('%s', '%d', '%d', '%d', '%d')" % (
                mem_data['Host'], mem_data['MemFree'], mem_data['MemUsage'], mem_data['MemTotal'], int(mem_data['Time']))
            cur.execute(mem_sql)
            cx.commit()
        except:
            pass
        print "RAM DB insert OK"
        # req = urllib2.Request("http://localhost:8888", json.dumps(data), {'Content-Type': 'application/json'})
        # f = urllib2.urlopen(req)
        # response = f.read()
        # print response
        # f.close()
        time.sleep(10)
