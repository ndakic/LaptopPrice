from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from . import prediction

import json
import pandas as pd


def index(request):
    return HttpResponse("Hello From Django!")

@csrf_exempt
def predictPrice(request):

	result = prediction.predict_price_mlr(prediction.create_dict(json.loads(request.body.decode("utf-8"))))

	return JsonResponse({'result': round(result[0], 2)})


