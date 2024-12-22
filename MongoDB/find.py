import pymongo


if __name__ == '__main__':
    my_client = pymongo.MongoClient('mongodb://localhost:27017/')
    my_db = my_client['mydatabase']
    my_col = my_db['customers']
    print(my_col.find_one())
    # value 0 will exclude that entity or attribute
    # o and 1 combination can only be used if _id is present
    for i in my_col.find({}, {'_id': 0, 'name': 1, 'address': 1}):
        print(i)
    for i in my_col.find({}, {'address': 0}):
        print(i)
