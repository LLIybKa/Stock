from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from .models import categorya,sklad_item,employee,postavka, otpravka
from .forms import OtpravkaForm
import requests
import simplejson as json

# Create your views here.


def index(reques):

	# category = categorya.objects.get(id=1)
	sklad_item_otobr = sklad_item.objects.all()
	mas = [1,2,3,4,5]
	name = 'Viktor Shubin'
	url = "https://api.telegram.org/bot885611551:AAGvMPrS2FRzj8nf7yqVUhYq00MTjfp7IDQ/sendMessage"
	args = {'name':name, 'mas':mas, 'sklad_item_otobr':sklad_item_otobr }
	data = {'chat_id': "372028584", 'text': "Привет", 'parse_mode': "HTML", 'disable_web_page_preview': "false"}
	headers = {'Content-type': 'application/json'}
	# sklad_item.objects.filter(col_vo_sklad = 0).delete()
	# vsphere_dict = dict(
	# 	'chat_id' = "372028584",
	# 	'text' = "Привет",
	# 	'parse_mode' = "HTML",
	# 	'disable_web_page_preview' = "false",
	# 	)
	# if sklad_item.objects.filter(col_vo_sklad = 0):
	# 	r = requests.post(url ,data = json.dumps(data), headers = headers)
		



	


	return render(reques, 'accounts/home.html', args)


 # def login(request):
 # 	return render(request, 'accounts/Login.html')

def detail(request, sklad_item_id):
	try:
		skl = sklad_item.objects.get(pk = sklad_item_id)	
	except:
		raise Http404('Эллемент не найден')

	return render(request,'accounts/detail.html',{'form': form,'sklad_item': skl})


def send(request, sklad_item_id):
	form = OtpravkaForm()
	otpravka_front = otpravka.objects.all()
	skl = sklad_item.objects.get(pk = sklad_item_id)
	if request.method == 'POST':
		form = OtpravkaForm(request.POST)
		if form.is_valid():
			form.save()
			take_col = int(skl.col_vo_sklad) - int(request.POST['col_vo_item'])
			skl.col_vo_sklad = take_col
			skl.save()

			return render(request,'accounts/send.html',{'sklad_item': skl})
	return render(request,'accounts/send.html',{'form': form,'sklad_item': skl, 'otpravka': otpravka_front})


def category(request):
	categorya_otobr = categorya.objects.all()
	cat = {'categorya_otobr': categorya_otobr}
	return render(request, 'accounts/category.html', cat)

def sotrudnik(request):
	sotrudnik_otobr = employee.objects.all()
	sat = {'sotrudnik_otobr': sotrudnik_otobr}
	return render(request, 'accounts/sotrudniki.html', sat)

def post(request):
	postavka_otobr = postavka.objects.all()
	post = {'postavka_otobr': postavka_otobr}
	return render(request, 'accounts/postavka.html', post)

def otpr(request):
	otpravka_otobr = otpravka.objects.all()
	otpr = {'otpravka_otobr': otpravka_otobr}
	return render(request, 'accounts/otpravka.html', otpr)






	


	




	
	



	




