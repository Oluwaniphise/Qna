from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from account.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
            login(request, user)
            
    context = {'form':form}
    
    return render(request, 'account/registration.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, f'Username or password is incorrect')

            
            return render(request, 'account/login.html')
    

   
    return render(request, 'account/login.html')



@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')


