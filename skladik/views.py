from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	mas = [1,2,3,4,5]
	name = 'Viktor Shubin'
	args = {'name':name, 'mas':mas}
	return render(request, 'accounts/home.html', args)


 # def login(request):
 # 	return render(request, 'accounts/Login.html')
