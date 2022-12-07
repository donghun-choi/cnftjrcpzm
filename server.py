from flask import *
import datetime as dt
import pymongo

def login():
    if 'user' in session:
        return True
    return False


TODAY = str(dt.datetime.now().month)+'월'+str(dt.datetime.now().day)+'일'

mongoDB_SERVER = pymongo.MongoClient("mongodb+srv://choidonghun:20060831@wms.9wulu4w.mongodb.net/?retryWrites=true&w=majority")
wmsDB = mongoDB_SERVER.wms

TODAYS_DATA_FORM_DB = wmsDB[TODAY]
STUDENTS_LIST_FROM_DB = wmsDB.student_list

stdl = STUDENTS_LIST_FROM_DB.find()

student_list = []

for x in stdl:
    student_list.append(x['name'])

student_list = set(student_list)
student_list = list(student_list)

print(student_list)



IDPW = wmsDB["회원 데이터베이스"]
app = Flask(__name__)
app.config['SECRET_KEY'] = f'asdfjrjh2rhhg;ah;h3lhtlqlhlk4r454blk23blkwbrlhb4lh2442j5h2'
app.config["PERMANENT_SESSION_LIFETIME"] = dt.timedelta(minutes=60)


@app.before_request
def limit_remote_addr():
    if '141.' in str(request.remote_addr): # West Taiwan
        abort(403,"TAIWAN IS COUNTRY")  # GET the FUCK out Tlqkf hahaha


PORT = 12342


@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('main'))

@app.route('/',methods=['POST',"GET"])
def main():
    TODAY = str(dt.datetime.now().month)+'월'+str(dt.datetime.now().day)+'일'
    if request.method == 'GET':
        if login():
            return render_template('main.html',StudentList = student_list, userName = session['user'])
        return render_template('login.html')
            
    elif request.method == 'POST':
        username_recive = request.form['userName']
        password = request.form['password']
        if not (username_recive and password):
            return render_template('login.html')
        
        result = IDPW.find_one({'password':password},{'userName':username_recive})
        print(result)
        if result is not None:
            session['user'] = username_recive
            return render_template('main.html', StudentList = student_list,userName = username_recive)
        else:
            flash("비밀번호나 ID를 다시 한번 확인해주세요")
            return render_template('login.html')
        

@app.route("/<name>", methods=['GET'])
def checkedName(name):
    if login():
        now = dt.datetime.now()
        TODAYS_DATA_FORM_DB = wmsDB[TODAY]
        CURRENT_TIME = str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        print(TODAY)
        data = {"name":name,"time":CURRENT_TIME,"checker":session['user']}
        print(data)
        TODAYS_DATA_FORM_DB.insert_one(data)
        return redirect(url_for('main'))
    else:
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