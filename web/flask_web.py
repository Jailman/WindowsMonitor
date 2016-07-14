#!C:\Python27\python.exe
# coding=utf-8


import sqlite3
import json
from flask import Flask, request, render_template, g
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    return render_template("mon.html")


@app.route("/cpu", methods=["GET"])
def getcpudata():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    cur.execute("SELECT `time`,`cpu_percent` FROM `cpu_stat`")
    ones = [[i[0] * 1000, i[1]] for i in cur.fetchall()]
    return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))


@app.route("/mem", methods=["GET"])
def getmemdata():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    cur.execute("SELECT `time`,`mem_usage` FROM `mem_stat`")
    ones = [[i[0] * 1000, i[1]] for i in cur.fetchall()]
    return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))

@app.route("/diskc", methods=["GET"])
def getdcdata():
    cx = sqlite3.connect("falcon.db")
    cur = cx.cursor()
    cur.execute("SELECT MAX(id),`disk_percent` FROM `diskc_stat`")
    ones = [["Used", i[1]] for i in cur.fetchall()]
    return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
