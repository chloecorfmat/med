from django.http import JsonResponse
from api.models import Person
from api.models import Day
from django.views.decorators.csrf import csrf_exempt
from api.services import ApiAuthorization
from django.conf import settings

import json
import datetime

@csrf_exempt
def day(request):
    if ApiAuthorization.check(request):
        # Create a day.
        if request.method == 'POST':
            try:
                data = request.body.decode('UTF-8')
                content = json.loads(data)
                person = Person.nodes.get(name=settings.PERSON_NAME)
                date = content.get('date')

                datetime_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
                print(datetime_obj)
                day = Day(date=datetime_obj).save()
                day.person.connect(person)

                response = day.to_json()
                return JsonResponse(response, safe=False)

            except:
                response = {"error": "Error occurred"}
                return JsonResponse(response, safe=False)

        if request.method == 'GET':
            try:
                content = request.GET
                date = content.get('date')
                datetime_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
                day = Day.nodes.get(date=datetime_obj)
                response = day.to_json()
                return JsonResponse(response, safe=False)
            except:
                response = {"error": "Error occurred"}
                return JsonResponse(response, safe=False)

def dayAll(request):
    if ApiAuthorization.check(request):
        if request.method == 'GET':
            try:
                days = Day.nodes.order_by('date')
                response = []
                for day in days:
                    obj = {
                        "id": day.id,
                        "date": day.date,
                        "dateFormatted": day.date.strftime('%Y-%m-%d'),
                        "comment": day.comment
                    }
                    response.append(obj)
                return JsonResponse(response, safe=False)
            except:
                response = {"error": "Error occurred"}
                return JsonResponse(response, safe=False)

@csrf_exempt
def dayComment(request):
    if ApiAuthorization.check(request):
        # Create a day.
        if request.method == 'POST':
            try:
                data = request.body.decode('UTF-8')
                content = json.loads(data)
                person = Person.nodes.get(name=settings.PERSON_NAME)
                date = content.get('date')
                comment = content.get('comment')

                datetime_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
                print(datetime_obj)
                day = Day.nodes.get(date=datetime_obj)
                day.comment = comment
                day.save()

                response = day.to_json()
                return JsonResponse(response, safe=False)

            except:
                response = {"error": "Error occurred"}
                return JsonResponse(response, safe=False)
