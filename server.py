from io import *
from flask import *
import datetime as dt
import pandas as pd
import pymongo
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def login():
    if 'user' in session:
        return True
    return False



LOGOUT_TIMER = 240
TODAY = str(dt.datetime.now().month)+'월'+str(dt.datetime.now().day)+'일'

mongoDB_SERVER = pymongo.MongoClient("mongodb+srv://choidonghun:20060831@wms.9wulu4w.mongodb.net/?retryWrites=true&w=majority")
wmsDB = mongoDB_SERVER.wms

TODAYS_DATA_FORM_DB = wmsDB[TODAY]
STUDENTS_LIST_FROM_DB = wmsDB.student_list

STUDENTS_LIST_FROM_DB = STUDENTS_LIST_FROM_DB.find()

student_list = []

for x in STUDENTS_LIST_FROM_DB:
    student_list.append(x['name'])

print("student_list",student_list)



IDPW = wmsDB["회원 데이터베이스"]
app = Flask(__name__)
app.config['SECRET_KEY'] = f'asdfjrjh2rhhg;ah;h3lhtlqlhlk4r454blk23blkwbrlhb4lh2442j5h2'
app.config["PERMANENT_SESSION_LIFETIME"] = dt.timedelta(minutes=LOGOUT_TIMER)


@app.before_request
def limit_remote_addr():
    if 'asdfasdfasdf' in str(request.remote_addr): # West Taiwan
        abort(403,"GET the FUCK out Tlqkf hahaha")  # GET the FUCK out Tlqkf hahaha

@app.route('/robots.txt')
def robot_to_root():
    return send_from_directory(app.static_folder, request.path[1:])


PORT = 12342


@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('main'))

isitlate = []

@app.route('/',methods=['POST',"GET"])
def main():
    TODAY = str(dt.datetime.now().month)+'월'+str(dt.datetime.now().day)+'일'
    # 리스트 방식으로 정렬함.
    todays_data = []
    todays_data_student = []
    todays_data_time = []
    Chedker_who = []
    isitlate = []

    for x in TODAYS_DATA_FORM_DB.find():
        if not "favicon.ico" in str(x):
            todays_data.append(x['name'])
            todays_data_student.append(x['name'])
            todays_data_time.append(x['time'])
            Chedker_who.append(x['checker'])
            isitlate.append(x['late'])
            

    if request.method == 'GET':
        if login():
            return render_template('main.html',isitlate=isitlate,StudentList = student_list, userName = session['user'],howmanyrecents = len(todays_data),todays_data_student = todays_data_student,todays_data_time = todays_data_time,Chedker_who=Chedker_who)
        return render_template('login.html')
            
    elif request.method == 'POST':
        username_recive = request.form.get('userName')
        password = request.form.get('password')
        if not (username_recive and password):
            print("비번입력을 안함")
            return render_template('login.html')
        resultID = IDPW.find_one({'userName':username_recive})
        resultPW = IDPW.find_one({'password':password})
        
        print("result",resultID)
        if resultID and resultPW is not None:
            session['user'] = username_recive
            return render_template('main.html',isitlate=isitlate,StudentList = student_list, userName = session['user'],howmanyrecents = len(todays_data),todays_data_student = todays_data_student,todays_data_time = todays_data_time,Chedker_who=Chedker_who)
        else:
            print("비번틀림")
            flash("비밀번호나 ID를 다시 한번 확인해주세요")
            return render_template('login.html')

@app.route("/<name>", methods=['GET'])
def checkedName(name):
    if login():
        if not name in student_list:
            flash("그건 우리 학생이 아닌데요?")
            return redirect(url_for("main"))
        late = False
        now = dt.datetime.now()
        TODAYS_DATA_FORM_DB = wmsDB[TODAY]
        CURRENT_TIME = str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        CTTSTR =int(str(now.hour)+str(now.minute))
        print(CTTSTR)
        if CTTSTR > 830 and CTTSTR < 1030: 
            late = True
        elif CTTSTR > 830:
            late = False
        print("TODAY",TODAY)
        data = {"name":name,"time":CURRENT_TIME,"checker":session['user'],"late":late}
        print("data",data)
        TODAYS_DATA_FORM_DB.insert_one(data)
        
        return redirect(url_for('main'))
    else:
        return redirect(url_for("main"))
@app.errorhandler(503)
def server_error(e):
    print('server_error 503')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


PORT = 12342
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, threaded=True, debug=True)