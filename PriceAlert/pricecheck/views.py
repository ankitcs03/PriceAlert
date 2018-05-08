from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . scrap import Fscrap, Ascrap


#from pricecheck.form import AlertForm
from . models import Alert
# Create your views here.
#from . priceCompare import priceCompare 

def index(request):
	return render(request, 'pricecheck/index.html')

def item(request):
	baseurl=""
	source = request.POST['location']
	item   = request.POST['q']
	price  = 0

	if (source == "Flipkart"):
		baseurl += "https://www.flipkart.com/search?q="
		baseurl += item.replace(' ','%20')
		price, prod_name = Fscrap(baseurl)

	else :
		baseurl += "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords="
		baseurl += item.replace(' ','%20')
		#price, prod_name = Ascrap(baseurl)
		return render(request, 'pricecheck/maintenance.html')
	
	return render(request, 'pricecheck/detail.html', {
		'source' : source,
		'item'   : item,
		'price'  : price,
		'prod_name' : prod_name,
		'baseurl' : baseurl
		})

def setAlert(request):
	if request.method == 'POST':
			finalurl = request.POST['baseurl']
			alert_obj = Alert(source = request.POST['source'], item=request.POST['item'] , url=finalurl, product_name=request.POST['prod_name'], alert_price=request.POST['alert_price'], email_id=request.POST['email_id'])
			alert_obj.save()
	else:
		pass
	return render(request, 'pricecheck/detail.html', { 'message': 'Alert set !!!'})


