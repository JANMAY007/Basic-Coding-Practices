import pymongo


if __name__ == '__main__':
    my_client = pymongo.MongoClient('mongodb://localhost:27017/')
    my_db = my_client['mydatabase']
    my_col = my_db['customers']
    my_query = {
        'name': 'Janmay'
    }
    my_doc = my_col.find(my_query)
    for i in my_doc:
        print(i)

    # to find name where name starts with 'B' or higher alphabets
    my_query = {
        "name": {"$gt": "B"}
    }
    my_doc = my_col.find(my_query)
    for i in my_doc:
        print(i)

    # name starts with 'B'
    my_query = {
        'name': {'$regex': '^B'}
    }
    my_doc = my_col.find(my_query)
    for i in my_doc:
        print(i)
