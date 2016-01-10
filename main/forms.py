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
        fields = '__all__'
        widgets = {
            'quest': forms.HiddenInput(attrs={'value': 1}),
            'date': forms.HiddenInput(),
            'time': forms.HiddenInput(),
            'cost': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'id': 'name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон', 'id': 'phone'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail', 'id': 'email'}),
        }