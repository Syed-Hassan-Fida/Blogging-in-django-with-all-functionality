from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from . import forms
# Create your views here.
def signup_view(request):
    # form = forms.signup()
    if request.method == 'POST':
        # form = forms.signup(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            print("user data",user)
            login(request, user)
            return redirect('blog:article')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blog:article')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form })
        
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blog:article')
