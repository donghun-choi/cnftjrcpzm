from flask import Flask, render_template, request
import pandas as pd
import datetime as dt
import pymongo

connect_to = pymongo.MongoClient("localhost",27017) # 로컬에서 열린 몽고디비 연결하기
targetDB = connect_to.new_Db # 몽고디비 안에 내가 원하는 디비 선택
collection = targetDB.members # 멤버라는 컬렉션에 연결

app = Flask(__name__)

PORT = 5000

today = str(dt.datetime.now().month)+str(dt.datetime.now().day)

names = ['me','you']

@app.route('/')
def index():
    return render_template('main.html', StudentList = names)


@app.route("/checked/<name>", methods=['GET'])
def checkedName(name):
    CURRENT_TIME = str(dt.datetime.now().hour)+':'+str(dt.datetime.now().minute)+':'+str(dt.datetime.now().second)
    data = {"name":name,"time":CURRENT_TIME}
    collection.insert_one(data) # 데이터 추가
    return render_template("checked.html", name=name,time = CURRENT_TIME)

    
    



@app.route('/overoll')
def overoll():
    return render_template('overoll.html', studentName ='ron')
    

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
  

if __name__ == "__main__":

    # app.run(port=PORT)
    app.run(port=PORT, debug=True)
    