from django.shortcuts import render
from django.http import HttpResponse

from myskool.models import MySkool


def skool(request):
    skool = MySkool.objects.all()

    context = {
        'skools' :skool,
    }
    
    return render(request, "skool.html", context)