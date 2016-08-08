from django import forms
from django.forms import DateField

states_and_uts = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
STATE_CHOICES = map(lambda x: (x, x), states_and_uts)
Country_Choices = ['India', 'Sorry only India']
COUNTRY_CHOICES = map(lambda x: (x, x), Country_Choices)


class PublisherForm(forms.Form):
    name = forms.CharField(max_length=25, label="name")
    address = forms.CharField(max_length=50, label="address")
    city = forms.CharField(max_length=30, label="city")
    state = forms.ChoiceField(widget=forms.Select, choices=STATE_CHOICES, label='state')
    country = forms.ChoiceField(widget=forms.Select, choices=COUNTRY_CHOICES, label="country")
    website = forms.URLField(max_length=40, label="website")


class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=15, label="first name")
    last_name = forms.CharField(max_length=15, label="last name")
    email = forms.EmailField(max_length=45, label="email")


class BookForm(forms.Form):
    title = forms.CharField(max_length=60, label="title")
    author = forms.CharField(max_length=30, label="author")
    publisher = forms.CharField(max_length=30, label="publisher")
    publishing_date = DateField(widget=forms.widgets.DateInput())