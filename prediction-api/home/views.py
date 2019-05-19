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

	params = json.loads(request.body.decode("utf-8"))

	data = [params['processorModel'], params['processorCores'], params['ramAmount'], params['storageType'], params['storageAmount'],
			params['ramGeneration'], params['condition'], params['screenSize'],]

	columns = ["processor_model", "cores", "ram_amount", "storage_type", "storage_amount", "ram_generation", "condition", "screen_size"]

	dataFrame = prediction.format_data(pd.DataFrame(data=[data], columns=columns))

	result, rmse = prediction.predict_price_mlr(dataFrame)

	return JsonResponse({'result': round(result[0]), "RMSE": round(rmse)})

