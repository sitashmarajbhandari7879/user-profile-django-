# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ProfileForm
from django.views.generic import TemplateView

def home(request):
	return HttpResponse("this is home")

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.profile.gender= form.cleaned_data.get('gender')
            user.profile.country = form.cleaned_data.get('country')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.street_name= form.cleaned_data.get('street_name')
            user.profile.street_number = form.cleaned_data.get('street_number')
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.contact = form.cleaned_data.get('contact')
            user.profile.profile_picture= form.cleaned_data.get('profile_picture')
            user.profile.job= form.cleaned_data.get('job')
            user.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Your profile was successfully edited.')
            return redirect('/home/')

    else:
        form = ProfileForm(instance=user, initial={
            'first_name':user.first_name,
            'last_name':user.last_name,
        	'gender':user.profile.gender,
            'country':user.profile.country,
            'city':user.profile.city,
            'street_name':user.profile.street_name,
            'street_number':user.profile.street_number,
            'bio':user.profile.bio,
            'birth_date':user.profile.birth_date,
            'contact':user.profile.contact,
            'profile_picture':user.profile.profile_picture,
            'job':user.profile.job,
            
            })
    return render(request, 'userprofile/profile.html', {'form': form})
    # return render(request, 'createprofile.html', {'form': form})

# class Temp(TemplateView):
#     template_name='createprofile.html'

 