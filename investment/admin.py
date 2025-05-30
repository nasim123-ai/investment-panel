from django.contrib import admin
from .models import InvestmentProject

admin.register(InvestmentProject)
class InvestmentProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "province", "city", "neighborhood_type", "area", "land_use", "residential_units", "commercial_units", "service_units", "investment_amount")
    search_fields = ("title", "province", "city")