from django import forms

from .models import Password, PasswordHeader


class PasswordForm(forms.ModelForm):

    class Meta:
        model = Password
        fields = ('pheader','site', 'ptail',)

class PasswordHeaderForm(forms.ModelForm):

    class Meta:
        model = PasswordHeader
        fields = ('title','hint', 'special_letter','etc')