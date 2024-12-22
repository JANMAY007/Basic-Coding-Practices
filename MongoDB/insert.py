import pymongo


if __name__ == '__main__':
    my_client = pymongo.MongoClient('mongodb://localhost:27017/')
    my_db = my_client['mydatabase']
    my_col = my_db['customers']
    my_dict = {
        "name": "Janmay",
        "address": "Bhavnagar"
    }
    my_data = my_col.insert_one(my_dict)
    print(my_data.inserted_id)
    # my_col.insert_one(my_dict)
    my_list = [
        {
            "name": "JanmayBhatt",
            "address": "Bhavnagar"
        },
        {
            "name": "BhattJanmay",
            "address": "Bhavnagar"
        }
    ]
    my_data = my_col.insert_many(my_list)
    print(my_data.inserted_ids)
    my_list = [
        {
            "_id": 1,
            "name": "JanmayBhatt",
            "address": "Bhavnagar"
        },
        {
            "_id": 2,
            "name": "BhattJanmay",
            "address": "Bhavnagar"
        }
    ]
    my_data = my_col.insert_many(my_list)
    print(my_data.inserted_ids)
