import pymongo


if __name__ == '__main__':
    my_client = pymongo.MongoClient('mongodb://localhost:27017/')
    my_db = my_client['mydatabase']
    my_col = my_db['customers']
    my_query = {
        'name': 'BhattJanmay'
    }
    print(my_col.delete_one(my_query))

    myquery = {
        "name": {"$regex": "^B"}
    }
    x = my_col.delete_many(myquery)
    print(x.deleted_count, " documents deleted.")

    x = my_col.delete_many({})
    print(x.deleted_count, " documents deleted.")
