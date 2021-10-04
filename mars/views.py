from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from dotenv import dotenv_values

API_KEY = str(dotenv_values(".env")["API_KEY"])

# Create your views here.
@csrf_exempt
def index(request):
    print(request.method)
    print(API_KEY)
    if request.method == "GET":
        return render(request, "index.html")
    else:
        r = requests.get(f"https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0")
        print(r.text)
        jsondata = json.dumps(json.loads(r.text))
        print(jsondata)
        context = {"resp": jsondata}
        return JsonResponse(context)