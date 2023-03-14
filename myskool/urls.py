from django.urls import path
from myskool.views import skool

urlpatterns = [
    path('skool/', skool),
]