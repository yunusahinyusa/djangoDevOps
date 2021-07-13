from django.http import Http404
from django.shortcuts import render
from  .models import database_conflicts, ssl_data


def index (request):
    result = database_conflicts()

    context = {

    "result" : result

    }


    #import pdb; pdb.set_trace()
    return  render(request,"index.html",context)
    #return  render(request,'index.html',{ 'result' :result})
