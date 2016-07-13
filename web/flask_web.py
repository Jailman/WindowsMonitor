#!C:\Python27\python.exe
# coding=utf-8


import sqlite3
import json
from flask import Flask, request, render_template, g
app = Flask(__name__)

# sqlite3 DB
# DATABASE = 'falcon.db'
# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = connect_to_database()
#     return db
#
# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()
# cur = get_db().cursor()


@app.route("/", methods=["GET", "POST"])
def hello():
    sql = ""
    if request.method == "POST":
        data = request.json
        try:
            sql = "INSERT INTO `mem_stat` (`host`,`mem_free`,`mem_usage`,`mem_total`,`time`) VALUES('%s', '%d', '%d', '%d', '%d')" % (
                data['Host'], data['MemFree'], data['MemUsage'], data['MemTotal'], int(data['Time']))
            ret = cur.execute(sql)
            cur.commit()
        except:
            pass
        return "OK"
    else:
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
