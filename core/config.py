import os
from sqlalchemy import create_engine

Database = dict(
    dialect=os.getenv('dialect'),
    driver=os.getenv('driver'),
    username=os.getenv('username'),
    password=os.getenv('password'),
    host=os.getenv('host'),
    database=os.getenv('database')
)
DatabaseLite = dict(
    dialect=str(os.getenv('DIALECTLITE', 'sqlite')),
    database=os.environ.get("DATABASELITE", 'ES.db')
)

MONGO_URI = f'{Database.get("dialect")}://{Database.get("username")}:{Database.get("password")}@{Database.get("host")}/{Database.get("database")}'
SQLITE_URI = f'{DatabaseLite.get("dialect")}:///{DatabaseLite.get("database")}'

db = create_engine(SQLITE_URI)

def wrap_response(data, errors=None):
    body = data
    if not errors:
        make_response = dict(
            data=body,
            status='OK'
        )
        return make_response
    else:
        make_response = dict(
            data=body,
            status='Failed'
        )
        return make_response
        