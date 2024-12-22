import pymongo


if __name__ == '__main__':
    my_client = pymongo.MongoClient('mongodb://localhost:27017/')
    my_db = my_client['mydatabase']
    my_col = my_db['customers']
    my_query = {
        'address': 'Bhavnagar'
    }
    new_query = {
        '$set': {'address': 'Ahmedabad'}
    }
    my_col.update_one(my_query, new_query)
    for x in my_col.find():
        print(x)

    my_query = {
        'address': 'Bhavnagar'
    }
    new_query = {
        "$set": {'name': 'BhattJanmay'}
    }
    x = my_col.update_many(my_query, new_query)
    print(x.modified_count, ' modified count')
