from django import db
import psycopg2
import pprint
from django.db import connection
import redis


def query_execute(query):
        with connection.cursor() as cursor:
            cursor.execute(query)
            db_query =  cursor.fetchall()
            pprint.pprint(db_query)
            print (type(db_query))
            return db_query
            
def ssl_data():
    response = query_execute('SELECT * FROM pg_stat_activity')
    print("%s", str(response))
    return response



