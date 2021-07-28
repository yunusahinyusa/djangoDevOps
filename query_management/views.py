from django.db import connection
from django.http import Http404
from django.shortcuts import render
from  .models import active_user, calls_pgStatUser, connection_number, database_conflicts, database_logs, dead_tuples, disk_usage, seq_tup_read, ssl_data, stat_replication, sum_deadlocks, tables_disk_usage, tables_rows, temp_bytes


def index (request):
    result = database_conflicts()
    replication = stat_replication()
    connectionum = connection_number()
    deadlock = sum_deadlocks()
    liverows = seq_tup_read()
    tempbytes = temp_bytes()  
    diskusage = disk_usage()
    activeuser = active_user()
    tablesusage = tables_disk_usage()
    usagelogs   = database_logs()
    tablesrows = tables_rows()
    deadtuples = dead_tuples()
    callsfunction = calls_pgStatUser()

    context = {

    "result" : result,
    "replication" : replication,
    "deadlock" : deadlock,
    "liverows" : liverows,
    "tempbytes" : tempbytes,
    "diskusage" : diskusage,
    "activeuser" : activeuser,
    "connectionnum" : connectionum,
    "tablesusage" : tablesusage,
    "usagelogs" : usagelogs,
    "tablesrows" : tablesrows,
    "deadtuples" : deadtuples,
    "callsfunction" : callsfunction


    }


    #import pdb; pdb.set_trace()
    return  render(request,"index.html",context)
    #return  render(request,'index.html',{ 'result' :result})
