from django.shortcuts import render, redirect, reverse
from django.contrib import auth,messages

# Create your views here.

def index(request):
    """Return the index.html file"""
    return render(request,'index.html')

'''Log user out'''
def logout(request):
    auth.logout(request)
    messages.success(request,'You have succesefully logged out')
    return redirect(reverse('index'))
    
