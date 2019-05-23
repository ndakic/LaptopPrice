from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from . import prediction

import json
import pandas as pd

# NOTE: columns order after drop: condition, cores, processor_model, ram_amount, ram_generation, screen_size, storage_amount, storage_type

columns = ["condition", "cores", "processor_model", "ram_amount", 'ram_generation', "storage_type"]

def index(request):
    return HttpResponse("Hello From Django!")

@csrf_exempt
def predictPriceMLR(request):

	params = json.loads(request.body.decode("utf-8"))

	data = [params['condition'],  params['processorCores'], params['processorModel'], params['ramAmount'], params['ramGeneration'], params['storageType']]

	dataFrame = prediction.format_data(pd.DataFrame(data=[data], columns=columns))

	result, rmse = prediction.predict_price_mlr(dataFrame)

	return JsonResponse({'result': round(result[0]), "RMSE": round(rmse)})

@csrf_exempt
def predictPriceKNN(request):

	params = json.loads(request.body.decode("utf-8"))

	data = [params['condition'], params['processorCores'], params['processorModel'], params['ramAmount'], params['ramGeneration'], params['storageType']]

	dataFrame = prediction.format_data(pd.DataFrame(data=[data], columns=columns))

	result, rmse = prediction.predict_price_knn(dataFrame)

	return JsonResponse({'result': round(result[0]), "RMSE": round(rmse)})