from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=1)
