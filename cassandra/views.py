from .models import connect_compactions, connect_gospinfo, connect_histogram, connect_info, connect_infos, connect_ring, connect_snapshots, connect_status, connect_tablestats, connect_tpstats
from django.shortcuts import render
from django.http import Http404


def cassandra_index (request):
    client_cassandra = connect_status()
    client_ping =  connect_ring()
    client_info = connect_info()
    client_tpstat = connect_tpstats()
    client_listsnapshot  = connect_snapshots()
    client_histograms = connect_histogram()
    client_ring = connect_ring()
    client_infos = connect_infos()
    client_compactions = connect_compactions()

    context = {
    "client_compactions" : client_compactions,
    "client_infos" : client_infos,
    "client_ring" : client_ring,
    "client_histograms" : client_histograms,
    "client_info" : client_info,
    "client_ping" : client_ping,
    "client_cassandra" : client_cassandra,
    "client_tpstat" : client_tpstat,
    "client_listsnapshot" : client_listsnapshot
    }

    #import pdb; pdb.set_trace()
    return  render(request,"index_cassandra.html",context)
    #return  render(request,'index.html',{ 'result' :result})


