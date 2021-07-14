from .models import connect_compactions, connect_gospinfo, connect_histogram, connect_info, connect_ring, connect_status, connect_tablestats, connect_tpstats
from django.shortcuts import render
from django.http import Http404


def cassandra_index (request):
    client_cassandra = connect_gospinfo()
    client_ping =  connect_ring()
    client_info = connect_info()
    context = {
    "client_info" : client_info,
    "client_ping" : client_ping,
    "client_cassandra" : client_cassandra

    }

    #import pdb; pdb.set_trace()
    return  render(request,"cassandra_index.html",context)
    #return  render(request,'index.html',{ 'result' :result})
