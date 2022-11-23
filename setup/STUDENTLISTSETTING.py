import pymongo


# connect_to = pymongo.MongoClient("localhost",27017) # 로컬에서 열린 몽고디비 연결하기
# targetDB = connect_to.wms # 몽고디비 안에 내가 원하는 디비 선택
# collection = targetDB.student_list # 멤버라는 컬렉션에 연결


client = pymongo.MongoClient("mongodb+srv://choidonghun:20060831@wms.9wulu4w.mongodb.net/?retryWrites=true&w=majority")
db = client.wms
collection = db.student_list


list1 = ["alex","alice","aylin","ch","clara","henry","j","nathan","noah","max","Ron","tw"] #학생 여기다 다 넣고 실행하면 됨.
# print (list1)
# for i in range(len(list1)):
data = {
    "name":list1[3],
}
collection.insert_one(data) # 데이터 추가

# a = collection.find_one('alex') #
# print (a)