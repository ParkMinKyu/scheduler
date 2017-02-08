# -- coding: utf-8 --
from dao import schedulerdao
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scheduler",methods=["GET","POST"])
def scheduler():
    if request.method == 'GET':
        print request
        start = request.args.get('start')
        end = request.args.get('end')
        return schedulerdao.getScheduler({'start':start , 'end' : end})

    if request.method == 'POST':
        schedule = {'title' : 'test', 'contents' : 'contents'}
        return  schedulerdao.setScheduler(schedule)

if __name__ =='__main__':
    app.run(debug=True)
