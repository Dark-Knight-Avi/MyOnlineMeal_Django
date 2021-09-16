from mealApp.models import Contact
from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    # return HttpResponse("This is Home Page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        ph = request.POST.get('ph')
        message = request.POST.get('message')
        contact = Contact(name = name, email = email, ph = ph, message = message)
        contact.save()
    return render(request, 'index.html')
# def services(request):
#     return render(request, '')