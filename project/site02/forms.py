from django import forms

PHONE_FIELD_REGEX = r'^\+?1?[\d\- ]{8,23}$'


class SignupForm(forms.Form):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label = "E-Mail")
    phone = forms.RegexField(regex=PHONE_FIELD_REGEX, label="Phone Number")
    dob = forms.DateField(label = "Date Of Birth")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")