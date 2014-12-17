__author__ = 'Stepan'
from django import forms
from main.models import GiftCardOrder, QuestOrder


class GiftCardOrderForm(forms.ModelForm):
    class Meta:
        model = GiftCardOrder
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'id': 'name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон', 'id': 'phone'}),
        }


class QuestOrderForm(forms.ModelForm):
    class Meta:
        model = QuestOrder