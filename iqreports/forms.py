__author__ = 'Stepan'
from django import forms
from main.models import Branch
from django.contrib.admin.widgets import AdminDateWidget


class ReportForm(forms.Form):
    startDate = forms.DateField(widget=AdminDateWidget(), label="Дата от")
    endDate = forms.DateField(widget=AdminDateWidget(), label="Дата до")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ReportForm, self).__init__(*args, **kwargs)
        profile = self.user.profile
        if self.user.is_superuser or not profile:
            model = forms.ModelChoiceField(queryset=Branch.objects.all(), required=True, label="Локации")
            self.fields['branch'] = model
            return
        if profile:
            branches_ids = list(map(lambda branch: branch.id, profile.branch.all()))
            self.fields['branch'] = \
                forms.ModelChoiceField(
                    queryset=Branch.objects.filter(id__in=branches_ids), required=True, label="Локации")
