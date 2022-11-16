from flask import Flask, render_template, request
import pandas as pd
import datetime as dt
import os.path
app = Flask(__name__)

PORT = 5000

today = str(dt.datetime.now().month)+str(dt.datetime.now().day)

names = ['me','you']

@app.route('/')
def index():
    return render_template('main.html', StudentList = names)


@app.route("/checked/<name>", methods=['GET'])
def ooaaa(name):
    CURRENT_TIME = str(dt.datetime.now().hour)+':'+str(dt.datetime.now().minute)+':'+str(dt.datetime.now().second)

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
    