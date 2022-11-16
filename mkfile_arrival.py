
import os.path
import pandas as pd
import datetime as dt
import time as t
CURRENT_DATA = str(dt.date.today().month)+"월"+str(dt.datetime.today().day)+"일"

student_list = pd.read_csv('./database/const/student_list.csv',names=['names'],encoding='CP949')

myList =  student_list['names'].values.tolist()


# df = pd.DataFrame([\x
#         ['', '','']],\
#         columns = ['DATE','NAME', 'ARRIVAL_TIME',])


    # print(i) # i = 이름들








df =[]
for names in myList:
    CURRENT_TIME = str(dt.datetime.today().hour)+":"+str(dt.datetime.today().minute)+":"+str(dt.datetime.today().second)
    df.append([names,CURRENT_TIME])
    # t.sleep(1)
print(df)

dataframe = pd.DataFrame(df,columns=['이름','도착시간'])
print(dataframe)

dataframe.to_csv('sample.csv')


today = str(dt.datetime.now().month)+str(dt.datetime.now().day)

defaultFilePath = 'database/csv/'
todaysFile = str(defaultFilePath+today+'.csv')

if os.path.exists(todaysFile):
    print(todaysFile)
else:
    print(todaysFile+'now ab')
    newFile = pd.DataFrame(columns=['이름','도착시간'])
    newFile.to_csv(todaysFile)
