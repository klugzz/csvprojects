from django.shortcuts import render
import csv
from django.http import HttpResponse
NAME=['abdul','bala','dinesh','arjun','loki']
AGE=[20,20,20,20,20]
SUB=['tamil','english','maths','sci','cs']

def store(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Dispositin']='attachment;filename=file.csv'
	writer=csv.writer(response)
	writer.writerow(['name','age','subject'])
	for (name,age,subject) in zip (NAME,AGE,SUB):
		writer.writerow([name,age,subject])
	return response
# Create your views here.
