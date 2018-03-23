from django.contrib import admin

from .models import *
# Register your models here.

# SU name = Stasello
# SU password = 19lSd70sex
#admin.site.register(Chocs)

@admin.register(Sets)
class SetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'image_tag', 'price')
    readonly_fields = ('image_tag',)

@admin.register(Candy)
class CandyAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(Bar)
class BarAdmin(admin.ModelAdmin):
    list_display = ("size", 'description', 'image_tag')

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('height', 'width', 'price')

@admin.register(ProductInBasket)
class ProductInBasketAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in ProductInBasket._meta.fields]
