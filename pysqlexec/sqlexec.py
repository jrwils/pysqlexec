import psycopg2
from psycopg2.extras import RealDictCursor
from sys import path as syspath
from os import path as ospath

syspath.append(ospath.dirname(__file__))
from dbconfig import dbs

# Register psycopg2 extension to return decimal values as float
DEC2FLOAT = psycopg2.extensions.new_type(psycopg2.extensions.DECIMAL.values,
                                         'DEC2FLOAT',
                                         lambda value, curs:
                                         float(value) if value is not None else None)
psycopg2.extensions.register_type(DEC2FLOAT)


def sqlexec(query, *args, **kwargs):
    database = kwargs.get('database')
    if database is None:
        database = 'default'

    conndb = dbs.get(database).get('dbname')
    connuser = dbs.get(database).get('dbuser')
    connpass = dbs.get(database).get('dbpass')
    connhost = dbs.get(database).get('dbhost')
    connport = dbs.get(database).get('dbport')

    conn = psycopg2.connect("dbname='{}' \
                             user='{}' \
                             password='{}' \
                             host='{}' \
                             port ='{}'".format(conndb,
                                                connuser,
                                                connpass,
                                                connhost,
                                                connport))

    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        if args:
            cur.execute(query, args[0])
        else:
            cur.execute(query)
        try:
            return_data = cur.fetchall()
        except:
            return_data = None
        conn.commit()
        conn.close()
        return return_data
    except Exception as e:
        conn.close()
        raise e
