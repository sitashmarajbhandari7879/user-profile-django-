from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

# signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'registration/registration_form.html',
                          {'form': form})

        else:
            #get data from SignUpForm using cleaned_data.get()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password,
                                     email=email)
            #whenever user signup, automatically sign in
            user = authenticate(username=username, password=password)
            login(request, user)
            
            #after signup redirect to home
            return redirect('profilecreate')

    else:
        return render(request, 'registration/registration_form.html',
                      {'form': SignUpForm()})

#logout
def logout_view(request):
    logout(request)
    return redirect('usersignup:login')