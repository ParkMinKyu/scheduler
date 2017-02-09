# -- coding: utf-8 --
# schedulerdao import
from dao import schedulerdao
from flask import Flask, request, render_template
app = Flask(__name__)

# 기본 페이지 접속
@app.route("/")
def index():
    return render_template("index.html")

# schedule 처리 get/post로 접근가능
@app.route("/scheduler",methods=["GET","POST"])
def scheduler():
    # 요청이 get이면
    if request.method == 'GET':
        # fullCalendar에서 start와 end를 yyyy-mm-dd 형식의 parameter로 넘겨준다.
        start = request.args.get('start')
        end = request.args.get('end')
        # schedulerdao.getScheduler에 start와 end를 Dictoionary형식으로 넘겨준다.
        return schedulerdao.getScheduler({'start':start , 'end' : end})

    #요청이 post면
    if request.method == 'POST':
        # Dictoionary 형식의 schedule 변수를 만든다. 추후 parameter를 받게 수정예정
        schedule = {'title' : 'test', 'contents' : 'contents'}
        # schedule을 입력한다.
        return  schedulerdao.setScheduler(schedule)

if __name__ =='__main__':
    app.run(debug=True)
