from django.conf.urls import url
from api.views import *
from django.urls import path

urlpatterns = [
    path('person', person),
    path('getAllPersons', getAllPersons),
    path('login', login),
    path('day', day),
    path('day/all', dayAll),
    path('pain', painEvaluation),
    path('pain-value', painEvaluationValue)
]