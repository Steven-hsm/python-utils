import pymongo
import _thread

myclient = pymongo.MongoClient("mongodb://192.168.106.128:27017/")

mydb = myclient["bigdata"]

mycollection = mydb["test"]

def insert_data():
    for i in range(10000):
        try:
            _thread.start_new_thread(insert_doc, ("thread"+str(i), 100))
        except:
            print("Error: 无法启动线程")

    print(mycollection.find().count())
    while 1:
        pass

def insert_doc(threadName, num):
    list = []
    for i in range(num):
        mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
        mydict['index'] = i
        mydict['name'] = mydict['name'] + str(i)
        list.append(mydict)
        # print(mydict)
    mycollection.insert_many(list)
    print("线程%s执行完毕\n" % threadName)
# insert_data()
list = mycollection.find({"index":1})

print(mycollection.find().count())

