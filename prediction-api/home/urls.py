from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict-price-mlr', views.predict_price_mlr, name='predictPriceMLR'),
    path('predict-price-knn', views.predict_price_knn, name='predictPriceKNN'),
]