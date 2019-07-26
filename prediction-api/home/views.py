from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from . import prediction

import json
import pandas as pd


columns = ["condition", "cores", "processor_model", "ram_amount", 'ram_generation', "storage_type"]


def index(request):
	return HttpResponse("Hello From Django!")


@csrf_exempt
def predict_price_mlr(request):
	params = json.loads(request.body.decode("utf-8"))

	data = [params['condition'],  params['processorCores'], params['processorModel'], params['ramAmount'],
			params['ramGeneration'], params['storageType']]

	user_input = prediction.transform_input(pd.DataFrame(data=[data], columns=columns))

	result, rmse = prediction.predict_price_mlr(user_input)

	return JsonResponse({'result': round(result[0]), "RMSE": round(rmse)})


@csrf_exempt
def predict_price_knn(request):

	params = json.loads(request.body.decode("utf-8"))

	data = [params['condition'], params['processorCores'], params['processorModel'],
			params['ramAmount'], params['ramGeneration'], params['storageType']]

	data_frame = prediction.format_data(pd.DataFrame(data=[data], columns=columns))

	result, rmse = prediction.predict_price_knn(data_frame)

	return JsonResponse({'result': round(result[0]), "RMSE": round(rmse)})
