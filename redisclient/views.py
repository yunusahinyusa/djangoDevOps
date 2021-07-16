from django.http import Http404
from django.shortcuts import render
from  .models import get_all_infos, get_memory_stats 

def redis_index (request):
    client_redis = get_all_infos()
    client_memory = get_memory_stats()
                   

    context = {

    "client_redis" : client_redis,
    "client_memory" :client_memory

    }


    #import pdb; pdb.set_trace()
    return  render(request,"redis_index.html",context)
    #return  render(request,'index.html',{ 'result' :result})