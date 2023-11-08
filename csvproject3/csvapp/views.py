from django.shortcuts import render
from csvapp.models import Student
import csv
from django.http import HttpResponse
def file(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename=student.csv'
	student=Student.objects.all()
	writer=csv.writer(response)
	writer.writerow(['NO','STUDENT','NAME','AGE','CITY'])
	for i in student:
		writer.writerow([i.no,i.name,i.age,i.city])
	return response
# Create your views here.
