import sqlite3
from sqlite3 import Error
from flask import current_app, g

def get_db():
    try:
        if 'db' not in g:
            g.db = sqlite3.connect("visageimage.db")
            g.db.row_factory = sqlite3.Row
        return g.db
    except Error:
        print( Error )


def close_db():
    db = g.pop( 'db', None )

    if db is not None:
        db.close()
