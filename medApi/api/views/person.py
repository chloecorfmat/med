from django.http import JsonResponse
from api.models import Person
from django.views.decorators.csrf import csrf_exempt
from api.services import ApiAuthorization

import json
from uuid import uuid4

def getAllPersons(request):
    if ApiAuthorization.check(request):
        if request.method == 'GET':
            try:
                persons = Person.nodes.all()
                response = []
                for person in persons :
                    obj = {
                        "name": person.name,
                    }
                    response.append(obj)
                return JsonResponse(response, safe=False)
            except:
                response = {"error": "Error occurred"}
                return JsonResponse(response, safe=False)
@csrf_exempt
def person(request):
    if request.method == 'GET':
        # get one person by name
        name = request.GET.get('name', ' ')
        try:
            person = Person.nodes.get(name=name)
            response = {
                "name": person.name,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        content = request.POST
        name = content.get('name')
        password = content.get('password')

        try:
            person = Person(name=name, password=password)
            person.save()
            response = {
                "name": person.name,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)