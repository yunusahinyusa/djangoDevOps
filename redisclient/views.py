from django.http import Http404
from django.shortcuts import render
from  .models import get_all_infos, get_client_output, get_info_clients, get_info_commandstats, get_info_replication, get_info_server, get_info_stats, get_memory, get_memory_stats 

def redis_index (request):
    client_commands =  get_info_commandstats()
    client_output   = get_client_output() 
    client_info = get_info_clients()   
    client_replication = get_info_replication()
    client_memory = get_memory()
    client_stats  = get_info_stats()
    
    
                   

    context = {

    "client_commands" : client_commands,
    "client_output" : client_output,
    "client_info" : client_info,
    "client_replication" : client_replication,
    "client_memory" : client_memory,
    "client_stats" : client_stats

    }


    #import pdb; pdb.set_trace()
    return  render(request,"redis_bootstrap.html",context)
    #return  render(request,'index.html',{ 'result' :result})