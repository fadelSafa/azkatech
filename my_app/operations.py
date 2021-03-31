from my_app.models import Vacation
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from datetime import date
import json


def add_user_vacation(user,description,date_from,date_to):
        vacation = Vacation()
        vacation.user = user
        vacation.description = description
        vacation.date_from = date_from
        vacation.date_to = date_to
        vacation.save()
        
        instance = {
            "id" : vacation.id,
            "description" : description,
            "date_from"  : date_from,
            "date_to" : date_to,
        }

        return JsonResponse({"instance":json.dumps(instance)},status=200) 

def delete_user_vacation(user,vacation_id):
    vacation = Vacation.objects.filter(id=vacation_id, user=user).first()
    if vacation:
        vacation.delete()
        instance = {
            "id" : vacation.id,
        }
        return JsonResponse({"instance":json.dumps(instance)},status=200)
    return JsonResponse({"error":"error"},status=404)

def update_user_vacation(user,vacation_id,description,date_from,date_to):
    vacation = Vacation.objects.get(user=user, id = vacation_id )
    vacation.description = description
    vacation.date_from = date_from
    vacation.date_to = date_to
    vacation.save()

    instance = {
            "id" : vacation.id,
            "description" : description,
            "date_from"  : date_from,
            "date_to" : date_to,
        }

    return JsonResponse({"instance":json.dumps(instance)},status=200) 
        