__author__ = 'Stepan'
from django import forms
from main.models import Branch
from django.contrib.admin.widgets import AdminDateWidget

branches = Branch.objects.all()
branch_choices = map(lambda branch: (branch.id, branch.address), branches)


class ReportForm(forms.Form):
    startDate = forms.DateField(widget=AdminDateWidget(), label="Дата от")
    endDate = forms.DateField(widget=AdminDateWidget(), label="Дата до")
    branch = forms.ChoiceField(initial='', widget=forms.Select(),
                               required=True, choices=branch_choices,
                               label="Локации")
    # class Meta:
    #     model = QuestOrder
    #     fields = '__all__'
    #     widgets = {
    #         'quest': forms.HiddenInput(attrs={'value': 1}),
    #         'date': forms.HiddenInput(),
    #         'time': forms.HiddenInput(),
    #         'cost': forms.HiddenInput(),
    #         'name': forms.TextInput(attrs={'placeholder': 'Имя', 'id': 'name'}),
    #         'phone': forms.TextInput(attrs={'placeholder': 'Телефон', 'id': 'phone'}),
    #         'email': forms.TextInput(attrs={'placeholder': 'E-mail', 'id': 'email'}),
    #     }