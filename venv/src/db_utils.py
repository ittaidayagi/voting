import pymongo
from config import config


def connect_to_collection(db_host, db_port,collection_name):
    config_values = config()
    myclient = pymongo.MongoClient("mongodb://{0}:{1}/".format(db_host,db_port))
    db =  myclient[config_values.get("DB_NAME")]
    if collection_name in db.collection_names():

        return db[collection_name]
    else:

        return False, "There is no such collection"

def query_collection(collection, query):

    if type(query) is not dict:
        return False, "Bad type for query"
    else:
        valid_keys = config().get("VALID_KEYS_TO_COLLECTION")[collection.name]
        if set(query.keys()).issubset(set(valid_keys)):
            curs = collection.find(query)
            results = []
            for c in curs:
                results.append(c)
            return results
        else:
            return False, "Invalid keys"

