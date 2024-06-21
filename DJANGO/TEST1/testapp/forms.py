from django import forms
from .models import Users
class registerform(forms.ModelForm):
    class Meta:
        model=Users
        fields=('username','password','confirmpassword')