from django.contrib import admin
from .models import product
from django.db.models import F
# Register your models here.

admin.site.site_header = 'Neu-Tech Website'
admin.site.site_title = 'Neu-Tech'
admin.site.index_title = 'Neu-Tech Administration'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc', 'seller_name')
    search_fields = ('name',)

    def price_discount(self,request,queryset):
        queryset.update(price=F('price') * 0.9)

    actions = (price_discount,)
    list_editable=('price','desc',)

admin.site.register(product,ProductAdmin)