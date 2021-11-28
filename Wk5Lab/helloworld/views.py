from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

import json
from pathlib import Path

# Create your views here.
def index(request):
    
    p = Path(__file__).with_name("data.txt")
    with p.open(encoding="utf8") as json_file:
        data = json.load(json_file)
        return HttpResponse(u'<html><body><pre>{}</pre></body></html>'.format(data["Message"]))
