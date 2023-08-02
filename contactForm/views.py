from django.http import HttpResponse
from django.shortcuts import render


def contactForm(request):
    return render(request, "contactForm.html")