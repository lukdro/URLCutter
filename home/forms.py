from django import forms
# from django.contrib.auth import get_user_model
from .models import UrlAddress, CSVFile
# from django.utils.translation import gettext, gettext_lazy as _

# from django.contrib.auth.forms import UserChangeForm, SetPasswordForm

# User = get_user_model()

class UrlAddressForm(forms.ModelForm):

    class Meta:
        model = UrlAddress
        fields = ["original_url"]


class CSVFileForm(forms.ModelForm):
    csvfile = forms.FileField()

    class Meta:
        model = CSVFile
        fields = ["csvfile"]