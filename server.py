from flask import Flask, render_template, request
import pandas as pd
import datetime as dt
import os.path
app = Flask(__name__)

PORT = 5000

today = str(dt.datetime.now().month)+str(dt.datetime.now().day)

defaultFilePath = 'database/csv/'
todaysFile = str(defaultFilePath+today+'.csv')

@app.route('/')
def index():
    student_list = pd.read_csv('./database/const/student_list.csv',\
    names=['names'],encoding='CP949')
    myList =  student_list['names'].values.tolist()
    print(myList)
    return render_template('main.html', myList=myList)


@app.route("/checked/<name>", methods=['GET'])
def ooaaa(name):
    CURRENT_TIME = str(dt.datetime.now().hour)+':'+str(dt.datetime.now().minute)+':'+str(dt.datetime.now().second)
    
    # return render_template("overoll.html", name=name) 이게 원래 방향 우선은 누르면 체크로 베타테스트 ㄱㄱ
    df = pd.read_csv(todaysFile)
    # df.add()
    # df.to_csv(todaysFile)
    print(df)
    return render_template("checked.html", name=name,time = CURRENT_TIME)

    
    



@app.route('/overoll')
def overoll():
    return render_template('overoll.html', studentName ='ron')
    

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


# 하루 지난거 감지하면 새 파일 만듦.

if os.path.exists(todaysFile):
    print(todaysFile)
else:
    print(todaysFile+'now ab')
    newFile = pd.DataFrame(columns=['이름','도착시간'])
    newFile.to_csv(todaysFile)

  

if __name__ == "__main__":

    # app.run(port=PORT)
    app.run(port=PORT, debug=True)
    