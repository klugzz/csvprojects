from django.shortcuts import render
from csvapp.models import Bank
from csvapp.forms import BankForm
import csv
from django.http import HttpResponse
def final(request):
	bank=Bank.objects.all()
	return render(request,'apps/final.html',{'s':bank})
def forms(request):
	form=BankForm()
	if request.method=="POST":
		form=BankForm(request.POST)
		if form.is_valid():
			form.save()
		return final(request)
	return render(request,'apps/form.html',{'form':form})
def file(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename=account.csv'
	bank=Bank.objects.all()
	writer=csv.writer(response)
	writer.writerow(['NO','NAME','AMOUNT','CITY'])
	for i in bank:
		writer.writerow([i.no,i.name,i.amount,i.city])
	return response
# Create your viws here.
