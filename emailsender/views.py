from django.shortcuts import render, redirect
from .models import Email
from psycopg2 import errors
from django.db.utils import IntegrityError

# Create your views here.

def add_email(request):

    email = request.POST.get('email-adress')
    
    if email != None:
        try:
            Email.objects.create(emailadress=email)
        except (errors.UniqueViolation, IntegrityError):
            return redirect('add-email')

    emaillist = Email.objects.all()

    context = {
        'email_list': emaillist,
    }

    return render(request, 'email.html', context)