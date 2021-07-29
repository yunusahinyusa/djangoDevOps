import os
from django.db import models
from os import initgroups
import subprocess
import pprint

def cassandra_connect(shell):
    output = os.popen(shell).read()
    print(output)
    print (type(output))
    x =  output.splitlines()
    print (type(x))
    return x

def connect_status():
    cmd = cassandra_connect("nodetool status")
    print("%s", str(cmd))
    cmd = [i.split() for i in cmd]
    cmd= cmd[5]
    cmd = [i.split() for i in cmd]
    result = []
    for r in cmd:
        result.append({"ip": r[0]})
    return result
    

#This command retrieves a list of active and pending tasks
def  connect_tpstats():
    cmd = cassandra_connect("nodetool tpstats")
    print("%s", str(cmd))
    print(type(cmd))
    #return [i.split(' ',1) for i in cmd]
    cmd = [i.split() for i in cmd]
    cmd = cmd[1:16]
    result = []
    for r in cmd:
        result.append({"pool": r[0], "active": r[1], "pending": r[2], "completed":r[3], "blocked":r[4],"all_blocked":r[5]})
    return result
    #return cmd[1:16]

    """
                    <tr> 
                <td>  {{ rise.pool }} </td>
                <td>  {{ rise.active }} </td>
                <td>  {{ rise.pending }} </td>
                <td>  {{ rise.completed }} </td>
                <td>  {{ rise.blocked }} </td>
                <td>  {{ rise.all_blocked }} </td>
                    </tr>
    """

#This command verifies if Cassandra is processing compactions fast enough
def  connect_compactions():
    cmd = cassandra_connect("nodetool compactionstats")
    print("%s", str(cmd))
    return cmd

#This command identifies the tables in which the number of SSTables is growing and 
#shows disk latencies and number of tombstones read per query
def  connect_tablestats():
    cmd = cassandra_connect("nodetool tablestats")
    print("%s", str(cmd))
    return cmd

#This command provides further information about tables with high latencies
def  connect_histogram():
    cmd = cassandra_connect("nodetool cfhistograms")
    print("%s", str(cmd))
    return cmd

def  connect_gospinfo():
    cmd = cassandra_connect("nodetool gossipinfo")
    print("%s", str(cmd))
    return cmd

def  connect_ring():
    cmd = cassandra_connect("nodetool ring")
    print("%s", str(cmd))
    return cmd

def  connect_info():
    cmd = cassandra_connect("nodetool info")
    print("%s", str(cmd))
    return cmd

def connect_snapshots():
    cmd = cassandra_connect("nodetool listsnapshots")
    print("%s", str(cmd))
    cmd = [i.split() for i in cmd]
    cmd = cmd[2:61]
    result = []
    for r in cmd:
        result.append({"snapshot_name": r[0], "keyspace_name": r[1], "column_name": r[2], "true_size":r[3], "size_disk":r[4]})
    return result
    #return cmd[1:16]
