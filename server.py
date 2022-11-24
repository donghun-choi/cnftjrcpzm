from flask import *
import pandas as pd
import datetime as dt
import pymongo

TODAY = str(dt.datetime.now().month)+'월'+str(dt.datetime.now().day)+'일'

# client = pymongo.MongoClient("localhost",27017) # 로컬에서 열린 몽고디비 연결하기

client = pymongo.MongoClient("mongodb+srv://id:pw@wms.9wulu4w.mongodb.net/?retryWrites=true&w=majority") # 원격
targetDB = client.wms # 몽고디비 안에 내가 원하는 디비 선택
TODAYS_DATA = targetDB[TODAY] # 멤버라는 컬렉션에 연결 

app = Flask(__name__)
app.secret_key = "My key"

# PORT = 12342 wms
PORT = 12342
# PORT = 5001 home

names = [
"alex","alice","aylin","ch","clara","henry",    
"j","nathan","noah","max","ron","tw"]


@app.route('/',methods=['POST',"GET"])
def main():
    TODAY = str(dt.datetime.now().month)+'월'+str(dt.datetime.now().day)+'일'
    # if 'id' in session:
    #     id = session['id']
    #     flash("weeee")
    return render_template('main.html', StudentList = names,userName = "UserName")
    # else:
    #     flash('login plz')
    #     return render_template('login.html')
    
app.route('login',methods = ['POST','GET'])
# def login():
#     if request.methods == 'POST':
#         session['userName'] = request.form['username']
#         return redirect(url_for('main'))
#     else:
#         return render_template('login.html')
    
    
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