from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict-price-mlr', views.predictPriceMLR, name='predictPriceMLR'),
    path('predict-price-knn', views.predictPriceKNN, name='predictPriceKNN'),
]