from django import db
from django.db import connection, models
import redis
import pprint
import config



def redis_connect(result) :
    redis_pool = None
    try :
        redis_pool = config.config(section="redis")
        # connect to the redis server
        print('Connecting to the redis server...')
        #ADD THE CONFIG FILE PARAMETER
        r = redis.StrictRedis(**redis_pool)
        data = r.execute_command(result)
        print("Query Answer:") 
        pprint.pprint(data)
        print (type(data))
        return data
    except Exception as e:
        print("something went wrong ")
        print(e)


def get_all_infos():
    result = redis_connect('info')
    print("%s", str(result))
    return result