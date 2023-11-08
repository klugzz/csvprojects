from django.contrib import admin
from csvapp.models import Bank
class BankAdmin(admin.ModelAdmin):
	list_display=['no','name','amount','city']
admin.site.register(Bank,BankAdmin)# Register your models here.
