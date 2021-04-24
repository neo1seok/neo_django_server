from django import forms

from .models import Webtoon,Portal


class WebtoonForm(forms.ModelForm):

    class Meta:
        model = Webtoon
        fields = ('portal','title')

class PortalForm(forms.ModelForm):

    class Meta:
        model = Portal
        fields = ('name','search_form')