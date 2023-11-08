from django.contrib import admin
from csvapp.models import Office
class OfficeAdmin(admin.ModelAdmin):
	list_display=['no','name','mobile','city','course']
admin.site.register(Office,OfficeAdmin)

# Register your models here.
