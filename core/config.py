import json
import os

from sqlalchemy import create_engine

__version__ = '0.9'

DatabaseLite = dict(
    dialect=str(os.getenv('DIALECTLITE', 'sqlite')),
    database=os.environ.get("DATABASELITE", ':memory:')
)

SQLITE_URI = f'{DatabaseLite.get("dialect")}:///{DatabaseLite.get("database")}'

db = create_engine(SQLITE_URI)

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
