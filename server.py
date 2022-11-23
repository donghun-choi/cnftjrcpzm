from flask import *
import pandas as pd
import datetime as dt
import pymongo

TODAY = str(dt.datetime.now().month)+str(dt.datetime.now().day)
print(TODAY)
connect_to = pymongo.MongoClient("localhost",27017) # 로컬에서 열린 몽고디비 연결하기
targetDB = connect_to.wms_shit # 몽고디비 안에 내가 원하는 디비 선택
TODAYS_DATA = targetDB.TODAY # 멤버라는 컬렉션에 연결

app = Flask(__name__)

# PORT = 12342 wms
PORT = 12342
# PORT = 5001 home


today = str(dt.datetime.now().month)+str(dt.datetime.now().day)

names = [
"alex","alice","aylin","ch","clara","henry",
"j","nathan","noah","max","Ron","tw"]


@app.route('/',methods=['POST',"GET"])
def main():
    return render_template('main.html', StudentList = names,userName = "UserName")

@app.route('/recent-arrival-departures')
def recent_arrival_departures():
    weee=TODAYS_DATA.find({})
    print(weee)
    return render_template('overoll.html')
    

@app.route("/<name>", methods=['GET'])
def checkedName(name):
    

    CURRENT_TIME = str(dt.datetime.now().hour)+':'+str(dt.datetime.now().minute)+':'+str(dt.datetime.now().second)
    data = {"name":name,"time":CURRENT_TIME}
    TODAYS_DATA.insert_one(data) # 데이터 추가

    return redirect(url_for('main'))



@app.route('/overoll')
def overoll():
    return render_template('overoll.html', studentName ='ron')
    

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
  

if __name__ == "__main__":

    # app.run(port=PORT)
    app.run(host="0.0.0.0", port=PORT, threaded=True, debug=True)    