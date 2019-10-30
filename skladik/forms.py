from django import forms

from .models import categorya, employee, postavka, sklad_item, otpravka

class OtpravkaForm(forms.ModelForm):

    class Meta:
        model = otpravka
        fields = ('item','col_vo_item', 'mesto_pribitiya', 'zakazchik_name','otpravka_date')