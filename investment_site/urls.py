from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("سلام! این صفحه اصلی پروژه شماست.")

urlpatterns = [
    path('', home), # صفحه اصلی
    path('admin/', admin.site.urls), # مسیر پنل مدیریت
]