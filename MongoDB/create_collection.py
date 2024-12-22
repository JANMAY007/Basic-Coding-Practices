import pymongo


if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]
    print(mydb.list_collection_names())
    print(mycol)
    collist = mydb.list_collection_names()
    if "customers" in collist:
        print("The collection exists.")
