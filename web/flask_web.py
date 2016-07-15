#!C:\Python27\python.exe
# coding=utf-8


import psutil
import sqlite3
import json
from flask import Flask, request, render_template, g
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("mon.html")

# 获取C盘用量

#
# @app.route("/diskc", methods=["GET"])
# def getdcdata():
#     cx = sqlite3.connect("falcon.db")
#     cur = cx.cursor()
#     cur.execute("SELECT MAX(id),`disk_percent` FROM `diskc_stat`")
#     used_percent = float(cur.fetchall()[0][1])
#     ones = [["Used", used_percent], ["Free", 100.0 - used_percent]]
#     return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))

# 获取CPU数据


@app.route("/cpu", methods=["GET"])
def getcpudata():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    cur.execute("SELECT `time`,`cpu_percent` FROM `cpu_stat`")
    ones = [[i[0] * 1000, i[1]] for i in cur.fetchall()]
    return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))

# 获取RAM数据


@app.route("/mem", methods=["GET"])
def getmemdata():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    cur.execute("SELECT `time`,`mem_usage` FROM `mem_stat`")
    ones = [[i[0] * 1000, i[1]] for i in cur.fetchall()]
    return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))

# 获取DiskIO数据


@app.route("/diskrio", methods=["GET"])
def getdriodata():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    cur.execute("SELECT `time`,`read_speed_kb` FROM `diskio_stat`")
    ones = [[i[0] * 1000, i[1]] for i in cur.fetchall()]
    return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))


@app.route("/diskwio", methods=["GET"])
def getdwiodata():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    cur.execute("SELECT `time`,`write_speed_kb` FROM `diskio_stat`")
    ones = [[i[0] * 1000, i[1]] for i in cur.fetchall()]
    return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))

# 获取网卡数据


@app.route("/nicsio", methods=["GET"])
def getnicsiodata():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    cur.execute("SELECT `time`,`sent_speed_kb` FROM `nicio_stat`")
    ones = [[i[0] * 1000, i[1]] for i in cur.fetchall()]
    return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))


@app.route("/nicrio", methods=["GET"])
def getnicriodata():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    cur.execute("SELECT `time`,`recv_speed_kb` FROM `nicio_stat`")
    ones = [[i[0] * 1000, i[1]] for i in cur.fetchall()]
    return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
