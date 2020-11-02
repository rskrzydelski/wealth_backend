import pymongo


def _get_db():
    cli = pymongo.MongoClient("mongodb://localhost:27017/")
    db = cli['market']
    return db


def _list_db():
    cli = pymongo.MongoClient("mongodb://localhost:27017/")
    dblist = cli.list_database_names()
    print(dblist)


def delete_db():
    cli = pymongo.MongoClient("mongodb://localhost:27017/")
    cli.drop_database('market')


def delete_doc(query):
    db = _get_db()

    if not db:
        return None

    try:
        db['metals'].delete_one(query)
    except pymongo.errors.ServerSelectionTimeoutError:
        print("ServerSelectionTimeoutError")


def get_doc(query):
    db = _get_db()

    if not db:
        return None

    try:
        doc = db['metals'].find_one(query)
    except pymongo.errors.ServerSelectionTimeoutError:
        print("ServerSelectionTimeoutError")
        doc = None

    return doc


def get_content():
    db = _get_db()

    if not db:
        return None

    try:
        documents = db['metals'].find()
    except pymongo.errors.ServerSelectionTimeoutError:
        print("ServerSelectionTimeoutError")
        documents = None

    return documents


def get_metal_price(name, unit, currency):
    db = _get_db()

    if not db:
        return None
    try:
        query = {'name': name, 'unit': unit, 'currency': currency}
        document = db['metals'].find_one(query)
    except pymongo.errors.ServerSelectionTimeoutError:
        print("ServerSelectionTimeoutError")
        document = None

    return document


def set_metal_price(name, unit, currency, value):
    db = _get_db()
    query = {'name': name, 'unit': unit, 'currency': currency}
    new_query = {"$set": {'name': name, 'unit': unit, 'currency': currency, 'value': value}}

    try:
        db['metals'].update_one(query, new_query, upsert=True)
    except pymongo.errors.ServerSelectionTimeoutError:
        print("ServerSelectionTimeoutError")
