from .models import connect_status
from django.shortcuts import render
from django.http import Http404


def cassandra_index (request):
    client_cassandra = connect_status()

    context = {

    "client_cassandra" : client_cassandra

    }

    #import pdb; pdb.set_trace()
    return  render(request,"cassandra_index.html",context)
    #return  render(request,'index.html',{ 'result' :result})
