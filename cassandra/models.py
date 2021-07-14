import os
from django.db import models
from os import initgroups
import subprocess
import pprint

def cassandra_connect(shell):
    
    output = os.popen(shell).read()
    print(output)
    print (type(output))
    return output


def connect_status():
    cmd = cassandra_connect("nodetool status")
    print("%s", str(cmd))
    return cmd