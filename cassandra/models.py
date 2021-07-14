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
    return x

def connect_status():
    cmd = cassandra_connect("nodetool status")
    print("%s", str(cmd))
    return cmd

#This command retrieves a list of active and pending tasks
def  connect_tpstats():
    cmd = cassandra_connect("nodetool tpstats")
    print("%s", str(cmd))
    return cmd

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
