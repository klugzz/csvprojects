from django.contrib import admin
from csvapp.models import Student
class StudentAdmin(admin.ModelAdmin):
	list_display=['no','name','age','city']
admin.site.register(Student,StudentAdmin)
# Register your models here.
