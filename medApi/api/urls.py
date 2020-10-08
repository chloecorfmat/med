from django.conf.urls import url
from api.views import *
from django.urls import path

urlpatterns = [
    path('person', person),
    path('getAllPersons', getAllPersons),
    path('login', login)
]