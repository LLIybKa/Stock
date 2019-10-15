from django.contrib import admin
from .models import categorya,sklad_item,employee,postavka, otpravka

admin.site.register(categorya)
admin.site.register(sklad_item)
admin.site.register(employee)
admin.site.register(postavka)
admin.site.register(otpravka)
