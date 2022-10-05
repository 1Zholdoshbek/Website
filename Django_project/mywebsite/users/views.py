from django.shortcuts import render
from django.contrib.auth.models import UserCreationForm

def register(request):
    form=UserCreationForm()
    return(request,'users/register.html',{'form':form})