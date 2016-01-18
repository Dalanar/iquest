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
