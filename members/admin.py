from django.contrib import admin
from .models import People

# Register your models here.

@admin.register(People)
class AdminArea(admin.ModelAdmin):
    list_display=['id', 'name', 'age', 'number', 'date', 'image', 'details']
