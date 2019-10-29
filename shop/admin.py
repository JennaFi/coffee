from django.contrib import admin
from .models import Coffee, Tea


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'sale', 'created', 'updated']
    list_filter = ['sale', 'created', 'updated']
    list_editable = ['price', 'sale']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tea)
class TeaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'sale', 'created', 'updated']
    list_filter = ['sale', 'created', 'updated']
    list_editable = ['price', 'sale']
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.