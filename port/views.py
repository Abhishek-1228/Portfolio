from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Email

def index(request):
    return render(request, 'port/index.html')

def submit(request):
    email=request.POST.get('email')
    print("email",email)
    if(email==''):
        return HttpResponse("Enter valid email")
    elif(email is not None):
        e=Email(email=email)
        e.save()
        return render(request, 'port/submit.html')
    else:
        return HttpResponse("Enter valid email")

    