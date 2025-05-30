from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("سلام! این صفحه اصلی پروژه شماست.")

urlpatterns = [
    path('', home),
]