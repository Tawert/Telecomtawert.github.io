from django.contrib import admin
from .models import House

@admin.register(House)
class AdminHouses(admin.ModelAdmin):
    list_display = ["name", "price"]
