from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.ModelForm):
        MALE='M'
        FEMALE='F'
        CHOICES=((MALE,"MALE"),(FEMALE,"FEMALE"),)

	first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', }),
        max_length=30,
        required=False)

	last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=False)

        gender=forms.ChoiceField(choices=CHOICES,required=True,)

	country = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False)

        city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False)

        street_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False) 

        street_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False)

	bio = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=500,
        required=False)

	birth_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'datepicker'},
        	),max_length=50,required=False)

	contact = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False)

        city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False)

        profile_picture=forms.ImageField(help_text="Upload image: ", required=False),

        job = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False)

	class Meta:
		model = Profile
		fields = ['first_name','last_name', 'profile_picture','contact','bio','job','gender','country','city','street_name','street_number']