from flask import *
from flask_login import *
import pandas as pd
import datetime as dt
import pymongo

TODAY = str(dt.datetime.now().month)+'월'+str(dt.datetime.now().day)+'일'
    
# client = pymongo.MongoClient("localhost",27017) # 로컬에서 열린 몽고디비 연결하기

client = pymongo.MongoClient("mongodb+srv://choidonghun:20060831@wms.9wulu4w.mongodb.net/?retryWrites=true&w=majority") # 원격
targetDB = client.wms # 몽고디비 안에 내가 원하는 디비 선택
TODAYS_DATA = targetDB[TODAY] # 멤버라는 컬렉션에 연결 
IDPW = targetDB["회원 데이터베이스"]
app = Flask(__name__)

# PORT = 12342 wms
PORT = 12342
# PORT = 5001 home 
# 5000번 포트는 AirPlay가 쓴다... 그걸로 지정하지마...

names = [
"alex","alice","aylin","ch","clara","henry",    
"j","nathan","noah","max","ron","tw"]


@app.route('/',methods=['POST',"GET"])
def main():
    TODAY = str(dt.datetime.now().month)+'월'+str(dt.datetime.now().day)+'일'
    # TODAY 여기서 안쓴다고 지우지 말것. 데이터베이스 업데이트 하는 용도로 쓰임. 자동으로 날자 업데이트된 데이터베이스 생성하는 용도.
    # 지우면 병신인증.
    return render_template('main.html', StudentList = names,userName = "UserName")


@app.route('/login',methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        print(id)
        print(password)
        IDPW.find()
        idspw = list(IDPW.find({'userName':id}, {'_id':False}))
        print(idspw)
    return render_template('login.html')
    
    
@app.route('/recent-arrival-departures')
def recent_arrival_departures():
    return render_template('overoll.html')


@app.route("/<name>", methods=['GET'])
def checkedName(name):
    TODAYS_DATA = targetDB[TODAY] # 멤버라는 컬렉션에 연결 
    CURRENT_TIME = str(dt.datetime.now().hour)+':'+str(dt.datetime.now().minute)+':'+str(dt.datetime.now().second)
    print(TODAY)
    data = {"name":name,"time":CURRENT_TIME}
    TODAYS_DATA.insert_one(data) # 데이터 추가
    return redirect(url_for('main'))


@app.errorhandler(503)
def server_error(e):
    print('server_error')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
  

if __name__ == "__main__":
    
    # app.run(port=PORT)
    app.run(host="0.0.0.0", port=PORT, threaded=True, debug=True)