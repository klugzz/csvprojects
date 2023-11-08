from django.shortcuts import render
from csvapp.models import Office
from csvapp.forms import OfficeForm
import csv
from django.http import HttpResponse
def final(request):
	office=Office.objects.all()
	return render(request,'apps/final.html',{'s':office})
def forms(request):
	form=OfficeForm()
	if request.method=="POST":
		form=OfficeForm(request.POST)
		if form.is_valid():
			form.save()
		return final(request)
	return render(request,'apps/form.html',{'form':form})
def file(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename=enquiry.csv'
	office=Office.objects.all()
	writer=csv.writer(response)
	writer.writerow(['NO','NAME','MOBILE','CITY','COURSE'])
	for i in office:
		writer.writerow([i.no,i.name,i.mobile,i.city,i.course])
	return response
def page(request):
	return render(request,'apps/page.html')
# Create your views here.
