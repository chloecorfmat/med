from django.http import JsonResponse
from api.models import Day
from api.models import PainEvaluation
from api.models import Person
from django.views.decorators.csrf import csrf_exempt
from api.services import ApiAuthorization

from django.conf import settings
import datetime
import json
from neomodel import db

@csrf_exempt
def painEvaluation(request):
    if ApiAuthorization.check(request):
        # Create a pain evaluation.
        if request.method == 'POST':
            try:
                data = request.body.decode('UTF-8')
                content = json.loads(data)
                date = content.get('date')
                datetime_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
                person = Person.nodes.get(name=settings.PERSON_NAME)

                # Create pain evaluation.
                days = Day.get_or_create({'date': datetime_obj}, relationship=person.days)

                value = content.get('value')
                type = content.get('type')

                pain_evaluation = PainEvaluation.get_or_create({'type': type}, relationship=days[0].pain_evaluations)[0]
                print(pain_evaluation)
                pain_evaluation.value = value
                pain_evaluation.save()
                print(pain_evaluation)

                response = {"success": "Pain evaluation created"}
                return JsonResponse(response, safe=False)
            except:
                response = {"error": "Error occurred"}
                return JsonResponse(response, safe=False)

def painEvaluationValue(request):
    if ApiAuthorization.check(request):
        # Create a pain evaluation.
        if request.method == 'GET':
            content = request.GET
            date = content.get('date')
            type = content.get('type')

            # MATCH (a:Day {date:"2020-10-11"})<-[:DURING]-(b:PainEvaluation {type: 'morning'})RETURN b.value
            query = "MATCH (a:Day {date:'" + date + "'})<-[:DURING]-(b:PainEvaluation {type: '" + type + "'})RETURN b.value"
            result = db.cypher_query(query)

            value = ''
            if result[0]:
                if result[0][0]:
                    if result[0][0][0]:
                        value = result[0][0][0]

            response = {
                'value': value
            }
            return JsonResponse(response, safe=False)