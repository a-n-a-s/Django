from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contacts
from django.contrib import messages

# Create your views here.


def index(request):
    # return HttpResponse("This Is a home page")

    return render(request, 'index.html')


def about(request):
    # return HttpResponse("This Is a About page")
    return render(request, 'about.html')


def services(request):
    # return HttpResponse("This Is a Services page")
    return render(request, 'services.html')


def contact(request):
    # return HttpResponse("This Is a Contact Page")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        con = Contacts(name=name,phone=phone,email=email,desc=desc,date = datetime.today() )
        con.save()
        messages.success(request,"Your Form Has Been Submitted")
    return render(request, 'contacts.html')
