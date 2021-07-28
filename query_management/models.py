from django import db
from django.http import response
import psycopg2
import pprint
from django.db import connection
import redis
import config
import re


def psql_connect(query):
    conn = None
    try:
        params = config.config(section="postgresql")
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(query)
        db_query =  cursor.fetchall()
        pprint.pprint(db_query)
        print (type(db_query))
        #db_query = re.sub(r'[^a-zA-Z0-9]','', db_query)
        return db_query
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            
def ssl_data():
    response = psql_connect('SELECT * FROM pg_stat_activity')
    print("%s", str(response))
    return response

#Showing information related to the current activity of that process
def procces_execute() :
    response = psql_connect('SELECT * FROM pg_stat_activity')
    print("%s", str(response))
    return response

#COLLECTED STATICS VIEWS
#Showing database-wide statistics about query cancels due to conflict with recovery on standby servers.
def database_conflicts() :
    response = psql_connect('SELECT * FROM pg_stat_database_conflicts')
    print("%s", str(response))
    result = []
    for r in response:
        result.append({"datid": r[0], "datname": r[1], "confl_space": r[2], "conf_lock":r[3], "conf_snapshot":r[4],"conf_buffer":r[5],"conf_deadlock":r[6]})
    return result

# number of connections
def connections_number() :
    response = psql_connect('SELECT sum(numbackends) FROM pg_stat_database')
    print("%s", str(response))
    return response

# Dİsk Usage Showing
def disk_usage() :
    response = psql_connect("SELECT pg_size_pretty(pg_database_size('postgres')) AS mydbsize")
    print("%s", str(response))
    result = []
    for r in response:
        result.append({"usage_disk": r[0]})
    return result

#Showing unique number of active users
def active_user() :
    response = psql_connect('SELECT datname, usename , COUNT(*) FROM pg_stat_activity GROUP BY datname, usename')
    print("%s", str(response))
    result = []
    for r in response:
        result.append({"base_name": r[0], "us_name": r[1], "count": r[2]})
    return result

#Displays statistics for each of the user tables.
def user_statics() :
    response = psql_connect('SELECT * FROM pg_stat_user_tables')
    print("%s", str(response))
    return response

#Block_usage
def block_usage() :
    response = psql_connect('SELECT * FROM pg_statio_user_tables')
    print("%s", str(response))
    return response

#You can also calculate a hit rate of blocks read from the shared buffer cache, using a query like this
def buffer_cache():
    response = psql_connect('SELECT sum(heap_blks_read) as blocks_read, sum(heap_blks_hit) as blocks_hit, sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as hit_ratio FROM pg_statio_user_tables')
    print("%s", str(response))
    return response

#number of total checkpoints occurring across all databases in your cluster 
def stat_writer() :
    response = psql_connect('SELECT * FROM pg_stat_bgwriter')
    print("%s", str(response))
    return response

#Connection metrics
#find the server’s current setting for the maximum number of connections
def count_connection() :
    response = psql_connect("SELECT setting::float FROM pg_settings WHERE name = 'max_connections'")
    print("%s", str(response))
    return response

#LOGS
#latest status of logs.
def database_logs() : 
    response = psql_connect('SELECT locktype, database, relation::regclass, mode, pid FROM pg_locks')
    print("%s", str(response))
    result = []
    for r in response:
        result.append({"lock_type": r[0], "database_result" : r[1],"relation_name":r[2],"mode_name":r[3],"pid":r[4]})
    return result


#PG_STAT_ALLTABLES
#Tables statics
def access_table() :
    response = psql_connect('SELECT * FROM pg_stat_all_tables')
    print("%s", str(response))
    return response

#Schema Names
def schema_names() :
    response = psql_connect('SELECT schemaname FROM pg_stat_all_tables')
    print("%s", str(response))
    return response

#Total number of deleted rows
def deleted_rows_count() :
    response = psql_connect('SELECT sum(n_tup_del) FROM pg_stat_all_tables')
    print("%s", str(response))
    return response

#Number of times it was analyzed manually
def manuel_analyze_count() :
    response = psql_connect('SELECT sum(analyze_count) FROM pg_stat_all_tables')
    print("%s", str(response))
    return response

#Number of times it was automatically analyzed
def auto_analyze_count() :
    response = psql_connect('SELECT sum(autoanalyze_count) FROM pg_stat_all_tables')
    print("%s", str(response))
    return response

#Last analyzed manually
def time_of_auto_analyze() :
    response = psql_connect('SELECT last_analyze FROM pg_stat_all_tables')
    print("%s", str(response))
    return response

#Total Number of Rows Added
def sum_of_tup() :
    response = psql_connect('SELECT sum(n_tup_ins) FROM pg_stat_all_tables')
    print("%s", str(response))
    return response

#Estimated number of dead rows
def dead_tup() :
    response = psql_connect('SELECT sum(n_dead_tup) FROM pg_stat_all_tables')
    print("%s", str(response))
    return response

#Estimated number of live rows
def rows_total() :
    response = psql_connect('SELECT sum(n_live_tup) FROM pg_stat_all_tables')
    print("%s", str(response))
    return response

#Total Number of Updated Rows
def updated_total_rows() :
    response = psql_connect('SELECT sum(n_tup_hot_upd) FROM pg_stat_all_tables')
    print("%s", str(response))
    return response


#PG_STAT_ALL_INDEXES
def stat_all_indexes() :
    response = psql_connect('SELECT * FROM pg_stat_all_indexes LIMIT 5')
    print("%s", str(response))
    return response

#OID's
def oids() :
    response = psql_connect('SELECT relid FROM pg_stat_all_tables')
    print("%s", str(response))
    return response

#PG_STATIO_ALL_TABLES
#Total number of disk blocks read from the table
def read_of_disk() :
    response = psql_connect('SELECT sum(heap_blks_read) FROM pg_statio_all_tables')
    print("%s", str(response))
    return response

#Number of buffer hits in this table
def buffer_hits() :
    response = psql_connect('SELECT sum(heap_blks_hit) FROM pg_statio_all_tables')
    print("%s", str(response))
    return response

#Number of total buffer hits in this table
def buffer_total_hits() :
    response = psql_connect('SELECT sum(heap_blks_hit) FROM pg_statio_all_tables')
    print("%s", str(response))
    return response 

#Number of disk blocks read from all indexes in the table
def table_read_disk_total() :
    response = psql_connect('SELECT sum(idx_blks_read) FROM pg_statio_all_tables')
    print("%s", str(response))
    return response

#Number of total buffer hits in all indexes on this table
def buffer_total_indexes() :
    response = psql_connect('SELECT sum(idx_blks_hit) FROM pg_statio_all_tables')
    print("%s", str(response))
    return response

#Total toast_blks_read
def toast_read() :
    response = psql_connect('SELECT sum(toast_blks_read) FROM pg_statio_all_tables')
    print("%s", str(response))
    return response

#Number of total buffer hits in this table's TOAST table (if any)
def toast_bloks_hit() :
    response = psql_connect('SELECT sum(toast_blks_hit) FROM pg_statio_all_tables')
    print("%s", str(response))
    return response

#Number of disk blocks read from this table's TOAST table indexes (if any)
def toast_read_blocks () :
    response = psql_connect('SELECT sum(tidx_blks_read) FROM pg_statio_all_tables')
    print("%s", str(response))
    return response 

#Total number of buffer hits in TOAST table indexes
def toast_tids_blocks() :
    response = psql_connect('SELECT sum(tidx_blks_hit) FROM pg_statio_all_tables')
    print("%s", str(response))
    return response


#PG_STAT_USER_FUNCTIONS
#Number of calls of the function
def calls_pgStatUser() :
    response = psql_connect('SELECT calls FROM pg_stat_user_functions')
    print("%s", str(response))
    return response

#Total time spent in this function and all other functions called by it, in milliseconds
def total_time_statUser() :
    response = psql_connect('SELECT total_time FROM pg_stat_user_functions')
    print("%s", str(response))
    return response

#Self_time
def self_time_statUser() :
    response = psql_connect('SELECT self_time FROM pg_stat_user_functions')
    print("%s", str(response))
    return response


#DATADOG VIEWS
#Replication Delay
def stat_replication() :
    response = psql_connect('SELECT EXTRACT(EPOCH FROM (now() - pg_last_xact_replay_timestamp()))::INT')
    #response = psql_connect('SELECT * FROM pg_stat_replication')
    #select now() - pg_last_xact_replay_timestamp() AS replication_delay;
    print("%s", str(response))
    result = []
    for r in response:
        result.append({"stat_replication": r[0]})
    return result

#Connection per database
def connection_number() :
    response = psql_connect('SELECT sum(numbackends) FROM pg_stat_database')
    print("%s", str(response))
    result = []
    for r in response:
        result.append({"connumber": r[0],})
    return result

#temp_bytes
def temp_bytes() :
    response = psql_connect('SELECT temp_bytes FROM pg_stat_database')
    print("%s", str(response))
    return response

#deadlocks
def sum_deadlocks() :

    response = psql_connect('SELECT sum(deadlocks) FROM pg_stat_database')
    print("%s", str(response))
    result = []
    for r in response:
        result.append({"sum_deadlock": r[0]})
    return result

#Number of live rows fetched by sequential scans
def seq_tup_read() :
    response = psql_connect('SELECT seq_tup_read FROM pg_stat_all_tables')
    print("%s", str(response))
    return response

def tables_disk_usage():
    response = psql_connect("SELECT nspname || '.' || relname AS relation, pg_size_pretty(pg_total_relation_size(C.oid)) AS total_size FROM pg_class C LEFT JOIN pg_namespace N ON (N.oid = C.relnamespace) WHERE nspname NOT IN ('pg_catalog', 'information_schema') AND C.relkind <> 'i' AND nspname !~ '^pg_toast' ORDER BY pg_total_relation_size(C.oid) DESC LIMIT 5")
    print("%s", str(response))
    result = []
    for r in response:
        result.append({"table_name": r[0], "disk_usage": r[1]})
    return result

def tables_rows():
    response = psql_connect("SELECT schemaname,relname,n_live_tup FROM pg_stat_user_tables ORDER BY n_live_tup DESC LIMIT 5")
    print("%s",str(response))
    result = []
    for r in response:
        result.append({"relname_table": r[1] , "schema_name" : r[0]})
    return result


def dead_tuples():
    response = psql_connect('SELECT relname, n_dead_tup FROM pg_stat_user_tables LIMIT 5')
    print("%s",str(response))
    result = []
    for r in response:
        result.append({"relaname": r[0], "total": r[1]})
    return result




