from django import forms
from deposit1.models import Deposit1


class Deposit1Form(forms.ModelForm):
    class Meta:
        model = Deposit1
        fields = [
            'deposit',
            'term',
            'rate',
            'interest',
        ]