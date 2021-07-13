from django import db
import psycopg2
import pprint
from django.db import connection
import redis
import config


def query_execute(query):
    conn = None
    try:
        params = config.config(section="postgresql")
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(query)
        db_query =  cursor.fetchall()
        pprint.pprint(db_query)
        print (type(db_query))
        return db_query
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            
def ssl_data():
    response = query_execute('SELECT * FROM pg_stat_activity')
    print("%s", str(response))
    return response

def database_conflicts() :
    response = query_execute('SELECT * FROM pg_stat_database_conflicts')
    print("%s", str(response))
    return response




