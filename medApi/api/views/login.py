from django.http import JsonResponse
from api.models import Person
from django.core.exceptions import PermissionDenied
from uuid import uuid4
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method == 'POST':
        content = request.POST
        name = content.get('name')
        password = content.get('password')

        try:
            person = Person.nodes.get(name=name)

            if person.password == password:
                token = uuid4()
                person.token = token
                person.save()
                response = {
                    "token": token,
                }
                return JsonResponse(response)
            else:
                raise PermissionDenied
        except:
            raise PermissionDenied
