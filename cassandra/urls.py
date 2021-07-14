from django.urls import path
from . import views


urlpatterns = [

    path("", views.cassandra_index, name="cassandra_index"),

]