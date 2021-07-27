from typing import List
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
        result = []
        if type(data) == bytes :
            m = data.decode('UTF-8')
            for line in m.split('b\n'):
                return line
        elif type(data) == List :
            print("Query Answer:") 
            pprint.pprint(data)
            print (type(data))
        print(type(data))
        return data


        
    except Exception as e:
        print("something went wrong ")
        print(e)


def get_all_infos():
    result = redis_connect('info')
    print("%s", str(result))
    result = result[result.find("'")+1:result.find("'")]
    return result

#This command returns an Array reply about the memory usage of the server.
def get_memory_stats():
    result = redis_connect('memory stats')
    print('%s' , str(result))
    return result

#General information about the Redis server
def get_info_server():
    result = redis_connect('info server')
    print("%s", str(result))
    return result

#Master/replica replication information
def get_info_replication():
    result = redis_connect('info replication')
    print('%s', str(result))
    return result

#CPU consumption statistics
def get_info_cpu():
    result = redis_connect('info cpu')
    print('%s', str(result))
    return result

#Redis command statistics
def get_info_commandstats():
    result = redis_connect('info commandstats')
    print('%s', str(result))
    return result

#Client connections section
def get_info_clients():
    result = redis_connect('info clients')
    print("%s" ,  str(result))
    #result = [x.encode('utf-8') for x in result]
    #str1 = ''.join(str(e) for e in result)
    #query = [i.split() for i in result]
    return result

#General statistics
def get_info_stats():
    result = redis_connect('info stats')
    print('%s' , str(result))
    return result

#RDB and AOF related information
def get_info_persistence():
    result = redis_connect('info persistence')
    print("%s" ,  str(result))
    return result


#This command provides an internal statistics report from the memory allocator. 
def get_memory_malloc():
    result = redis_connect('memory malloc-stats')
    print('%s' , str(result))
    return result

#You can collect all 
#memory utilization metrics data for a Redis instance by running “info memory”.
def get_memory():
    result = redis_connect('info memory')
    print('%s' , str(result))
    return result

#This makes the slow log remarkably 
#fast at the point that you can enable the logging of all the commands 
def get_slowlog():
    result = redis_connect('slowlog get 2')
    print('%s', str(result))
    return result

#The LATENCY HISTORY command returns the raw data of the event 's latency spikes time series.
def get_latency():
    result = redis_connect('latency history command')
    print('%s' , str(result))
    return result

def get_client_output():
    result = redis_connect('CLIENT LIST')
    print('%s' , str(result))
    return result

