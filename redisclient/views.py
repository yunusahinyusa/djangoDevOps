from django.http import Http404
from django.shortcuts import render
from  .models import get_all_infos

def redis_index (request):
    client_redis = get_all_infos()

    context = {

    "client_redis" : client_redis

    }


    #import pdb; pdb.set_trace()
    return  render(request,"redis_index.html",context)
    #return  render(request,'index.html',{ 'result' :result})