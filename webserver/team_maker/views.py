from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import FaceitPost


def index(request):
    return HttpResponse("TEAM MAKER ROOT PAGE")

@csrf_exempt
def faceit_input(request):
    print(request.body)
    f = FaceitPost(date=timezone.now(), json_body=request.body )
    f.save()

    return HttpResponse("processed")

