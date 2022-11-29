from flask import *
import datetime as dt
import pymongo
import pandas as pd

def login1():
    if 'user' in session:
        return True
    return False



TODAY = str(dt.datetime.now().month)+'월'+str(dt.datetime.now().day)+'일'

mongodb_href = open('./mongodbkey.txt', 'r')
client = pymongo.MongoClient("mongodb+srv://choidonghun:20060831@wms.9wulu4w.mongodb.net/?retryWrites=true&w=majority")
targetDB = client.wms
TODAYS_DATA = targetDB[TODAY]
IDPW = targetDB["회원 데이터베이스"]
app = Flask(__name__)
secret_key = open('./key.txt','r')
key = secret_key.read()
app.config['SECRET_KEY'] = key
app.config["PERMANENT_SESSION_LIFETIME"] = dt.timedelta(minutes=15)

PORT = 12342
names = ['me','you']

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('main'))

@app.route('/',methods=['POST',"GET"])
def main():
    TODAY = str(dt.datetime.now().month)+'월'+str(dt.datetime.now().day)+'일'
    if request.method == 'GET':
        if login1():
            return render_template('main.html',StudentList = names, userName = session['user'])
        return render_template('login.html')
            
    elif request.method == 'POST':
        username_recive = request.form['userName']
        password = request.form['password']
        if not (username_recive and password):
            flash("모두 입력해주세요")
            return render_template('login.html')
        
        result = IDPW.find_one({'password':password},{'userName':username_recive})
        print(result)
        if result is not None:
            session['user'] = username_recive
            return render_template('main.html', StudentList = names,userName = username_recive)
        else:
            flash("비밀번호나 ID를 다시 한번 확인해주세요")
            return render_template('login.html')
    

@app.route('/recent-arrival-departures')
def recent_arrival_departures():
    if login1():
        return render_template('overoll.html',userName = session['user'])
    else:
        return redirect(url_for('main'))


@app.route("/<name>", methods=['GET'])
def checkedName(name):
    TODAYS_DATA = targetDB[TODAY]
    CURRENT_TIME = str(dt.datetime.now().hour)+':'+str(dt.datetime.now().minute)+':'+str(dt.datetime.now().second)
    print(TODAY)
    data = {"name":name,"time":CURRENT_TIME}
    TODAYS_DATA.insert_one(data)
    return redirect(url_for('main'))


@app.errorhandler(503)
def server_error(e):
    print('server_error 503')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
  

PORT = 12342
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, threaded=True, debug=True)