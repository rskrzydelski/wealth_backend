import pymongo


def _get_db():
    cli = pymongo.MongoClient("mongodb://localhost:27017/")
    db = cli['market']
    return db


def _list_db():
    cli = pymongo.MongoClient("mongodb://localhost:27017/")
    dblist = cli.list_database_names()
    print(dblist)


def _delete_db():
    cli = pymongo.MongoClient("mongodb://localhost:27017/")
    cli.drop_database('market')


def get_metal_price(name):
    db = _get_db()

    if not db:
        return None

    try:
        document = db['metals'].find_one({name: {"$exists": True}})
    except pymongo.errors.ServerSelectionTimeoutError:
        print("ServerSelectionTimeoutError")
        document = None

    return document


def set_metal_price(name, value, currency, unit):
    db = _get_db()
    query = {name: {"$exists": True}}
    new_query = {"$set": {name: value, 'currency': currency, 'unit': unit}}

    try:
        db['metals'].update_one(query, new_query, upsert=True)
    except pymongo.errors.ServerSelectionTimeoutError:
        print("ServerSelectionTimeoutError")








