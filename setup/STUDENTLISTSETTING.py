import pymongo

connect_to = pymongo.MongoClient("localhost",27017) # 로컬에서 열린 몽고디비 연결하기
targetDB = connect_to.wms_shit # 몽고디비 안에 내가 원하는 디비 선택
collection = targetDB.student_list # 멤버라는 컬렉션에 연결
list1 = ["alex","alice","aylin","ch","clara","henry","j","nathan","noah","max","Ron","tw"] #학생 여기다 다 넣고 실행하면 됨.
# print (list1)
# for i in range(len(list1)):
#     data = {
#         "name":list1[i],
#     }
#     collection.insert_one(data) # 데이터 추가

print(collection)