from django.conf import settings
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
	path('', views.index, name = 'index'),
	path('detail/<int:sklad_item_id>/', views.detail , name = 'detail'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('send/<int:sklad_item_id>/', views.send, name = 'send'),
	path('category/', views.category, name = 'category'),
	path('sotrudnik/', views.sotrudnik, name = 'sotrudnik'),
	path('postavka/', views.post, name = 'post'),
	path('otpravka/', views.otpr, name = 'otpr'),

]