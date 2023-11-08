from django.shortcuts import render
from csvapp.models import Product
import csv
from django.http import HttpResponse

def store(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename=product.csv'
	product=Product.objects.all()
	writer=csv.writer(response)
	writer.writerow(['NO','PRODUCTNAME','PRICE','WARENTY','STOCK'])
	for i in product:
		writer.writerow([i.no,i.name,i.price,i.warenty,i.stock])
	return response
# Create your views here.:
