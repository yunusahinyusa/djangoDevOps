from django.urls import path
from . import views


urlpatterns = [

    path("", views.redis_index, name="redis_index"),

]