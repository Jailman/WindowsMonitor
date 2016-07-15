#!C:\Python27\python.exe
# coding=utf-8

import time
import socket
import psutil
import sqlite3
import threading

host = socket.gethostname()

class nioThread (threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        nicio_mon()


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
        nio_data["Sent_speed_kb"] = int(sent_end_byte - sent_start_byte)/1024
        nio_data["Recv_speed_kb"] = int(recv_end_byte - recv_start_byte)/1024
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
    nioThread = nioThread()
    nioThread.start()
