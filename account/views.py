from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.
def account(request):
    return render(request, 'account.html')



def form(request):
    # if request.method =='POST':
    #     form =UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('homepage:index')

    # else:
    #     form = UserCreationForm()        
    return render(request,'form.html',) 

def register(request):
    form =CreateUserForm
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username =form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}!')
            form.save()
            return redirect('account')

    return render(request,'register.html', {'form':form})       
