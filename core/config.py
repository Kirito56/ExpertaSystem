import json
import os

from pymongo import MongoClient
from sqlalchemy import create_engine

Database = dict(
    dialect=os.getenv('dialect', 'mongodb'),
    driver=os.getenv('driver', 'srv'),
    username=os.getenv('username', 'Solus'),
    password=os.getenv('password', 'H0v55E3q8i8DjvqOdGy3'),
    host=os.getenv('host', 'rocketchat.6olwp.mongodb.net'),
    database=os.getenv('database', 'Experta_System')
)
DatabaseLite = dict(
    dialect=str(os.getenv('DIALECTLITE', 'sqlite')),
    database=os.environ.get("DATABASELITE", ':memory:')
)

MONGO_URI = f'{Database.get("dialect")}+{Database.get("driver")}://{Database.get("username")}:{Database.get("password")}@{Database.get("host")}'
SQLITE_URI = f'{DatabaseLite.get("dialect")}:///{DatabaseLite.get("database")}'

db = create_engine(SQLITE_URI)
client = MongoClient(MONGO_URI)
mongo = client['Experta_System']
series_collection = mongo['ES']
series_collection_rule = mongo['Rules']


def wrap_response(data, errors=None):
    body = data
    if not errors:
        make_response = dict(
            data=body,
            status='OK'
        )
        return json.dumps(make_response, sort_keys=True)
    else:
        make_response = dict(
            data=body,
            status='Failed'
        )
        return json.dumps(make_response, sort_keys=True)


def insert_document(collection, data: dict):
    """[summary]

    Args:
        collection ([type]): [description]
        data (dict): [description]
    """
    return collection.insert_one(data).inserted_id


def find_document(collection, elements, multiple=False):
    """ Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements.
    """
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)


def update_document(collection, query_elements, new_values):
    """ Function to update a single document in a collection.
    """
    collection.update_one(query_elements, {'$set': new_values})


def delete_document(collection, query):
    """ Function to delete a single document from a collection.
    """
    collection.delete_one(query)
