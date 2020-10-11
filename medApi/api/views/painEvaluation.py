from django.http import JsonResponse
from api.models import Day
from api.models import PainEvaluation
from api.models import Person
from django.views.decorators.csrf import csrf_exempt
from api.services import ApiAuthorization

from django.conf import settings

import datetime

@csrf_exempt
def painEvaluation(request):
    if ApiAuthorization.check(request):
        # Create a pain evaluation.
        if request.method == 'POST':
            try:
                content = request.POST
                date = content.get('date')
                datetime_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
                person = Person.nodes.get(name=settings.PERSON_NAME)

                # Create pain evaluation.
                days = Day.get_or_create({'date': datetime_obj}, relationship=person.days)

                value = content.get('value')
                type = content.get('type')

                pain_evaluation = PainEvaluation(type=type, value=value).save()
                pain_evaluation.day.connect(days[0])

                response = {"success": "Pain evaluation created"}
                return JsonResponse(response, safe=False)
            except:
                response = {"error": "Error occurred"}
                return JsonResponse(response, safe=False)
