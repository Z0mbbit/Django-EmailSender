from django.shortcuts import render, redirect
from .models import Email

# Create your views here.

def add_email(request):

    email = request.POST.get('email-adress')
    if email != None:
        Email.objects.create(emailadress=email)

    emaillist = Email.objects.all()

    context = {
        'email_list': emaillist,
    }

    return render(request, 'email.html', context)