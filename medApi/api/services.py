from django.core.exceptions import PermissionDenied
from django.core.serializers.json import DjangoJSONEncoder
from api.models import Person
from api.models import Day

class ApiAuthorization:

    @staticmethod
    def check(request):
        try:
            token = request.headers.get('Authorization')
            person = Person.nodes.get(token=token)
            return True
        except:
            raise PermissionDenied
