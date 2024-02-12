from django.shortcuts import render
from accounts.form import RegistrationsForm


# Create your views here.
def register(request):
    form =RegistrationsForm()
    context ={
        'form':form
    }
    return render(request,'accounts/register.html',context)

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return render(request,'accounts/logout.html')