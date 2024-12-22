import pymongo


if __name__ == '__main__':
    my_client = pymongo.MongoClient('mongodb://localhost:27017/')
    my_db = my_client['mydatabase']
    my_col = my_db['customers']
    my_doc = my_col.find().sort("name", 1)  # 1 for ascending and -1 for descending
    for x in my_doc:
        print(x)
