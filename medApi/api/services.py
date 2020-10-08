from django.core.exceptions import PermissionDenied
from api.models import Person

class ApiAuthorization:

    @staticmethod
    def check(request):
        try:
            token = request.headers.get('Authorization')
            person = Person.nodes.get(token=token)
            return True
        except:
            raise PermissionDenied