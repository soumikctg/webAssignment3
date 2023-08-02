from django.http import HttpResponse
from django.shortcuts import render
from contact.models import formData

def contactForm(request):
    return render(request, "contactForm.html")

def saveForm(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        message = request.POST.get('message')
        data=formData(name=name, email=email, phone=phone, address=address, message=message)
        data.save()
    
    return render(request, "contactForm.html")