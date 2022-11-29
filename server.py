from flask import *
from flask_login import *
import datetime as dt
import pymongo

TODAY = str(dt.datetime.now().month)+'월'+str(dt.datetime.now().day)+'일'
client = pymongo.MongoClient("mongodb+srv://choidonghun:20060831@wms.9wulu4w.mongodb.net/?retryWrites=true&w=majority") # 원격
targetDB = client.wms
TODAYS_DATA = targetDB[TODAY]
IDPW = targetDB["회원 데이터베이스"]
app = Flask(__name__)
PORT = 12342
names = [
"alex","alice","aylin","ch","clara","henry",    
"j","nathan","noah","max","ron","tw"]


@app.route('/',methods=['POST',"GET"])
def main():
    TODAY = str(dt.datetime.now().month)+'월'+str(dt.datetime.now().day)+'일'
    return redirect("/login")
    return render_template('main.html', StudentList = names,userName = "UserName")


@app.route('/login',methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_recive = request.form['userName']
        password = request.form['password']
        print(username_recive)
        print(password)
        result = IDPW.find_one({'password':password},{'userName':username_recive})
        print(result)
        
        if result is not None:
            print('login')

    return render_template('login.html')
    
    
@app.route('/recent-arrival-departures')
def recent_arrival_departures():
    return render_template('overoll.html')


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