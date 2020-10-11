from django.http import JsonResponse
from api.models import Person
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = request.body.decode('UTF-8')
        content = json.loads(data)
        name = content.get('name')
        password = content.get('password')

        try:
            person = Person.nodes.get(name=name)

            if person.password == password:
                response = {
                    "token": person.token,
                }

                return JsonResponse(response)
            else:
                raise PermissionDenied
        except:
            raise PermissionDenied
