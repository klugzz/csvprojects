from django.contrib import admin
from csvapp.models import Product
class ProductAdmin(admin.ModelAdmin):
	list_display=['no','name','price','warenty','stock']
admin.site.register(Product,ProductAdmin)
# Register your models here.
