import pymongo


if __name__ == '__main__':
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = my_client["mydatabase"]
    my_col = my_db["customers"]
    my_result = my_col.find().limit(5)
    for x in my_result:
        print(x)
