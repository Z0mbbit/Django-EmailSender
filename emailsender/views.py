from django.shortcuts import render, redirect
from .models import Email
from psycopg2 import errors
from django.db.utils import IntegrityError
from django.core.mail import BadHeaderError, send_mass_mail
from main.settings import EMAIL_HOST_USER



def add_email(request):
    # Function to add an email address and return a list of all email objects
    
    email = request.POST.get('email-adress')
    
    if email != None:
        try:
            Email.objects.create(emailadress=email)
        except (errors.UniqueViolation, IntegrityError):
            return redirect('add-email')

    subject = request.POST.get("subject")
    message = request.POST.get("message")
    to_email_list = request.POST.getlist("receiver_input")

    datatuple = ()

    if subject and message and to_email_list:
        try:
            for mail in to_email_list:
                data = (subject, message, EMAIL_HOST_USER, [mail])
                datatuple += (data,)
            #print(datatuple)
            send_mass_mail(datatuple)
        except BadHeaderError:
            return redirect('add-email')
    
    
    emaillist = Email.objects.all()

    context = {
        'email_list': emaillist,
    }

    return render(request, 'email.html', context)

# def send_mail(request):
#     # Function to send mails

#     from_email = request.POST.get("email")
#     subject = request.POST.get("subject")
#     message = request.POST.get("message")
#     to_email_list = request.POST.get("receiver_input")

#     print('Hallo')
#     print(from_email)
#     print(subject)
#     print(message)
#     print(to_email_list)

    
#     if subject and message and from_email and to_email_list:
#         try:
#             datatuple = ()

#             for mail in to_email_list:
#                 datatuple += (subject, message, from_email, mail)

#             print(datatuple)
#             send_mass_mail(datatuple)
#         except BadHeaderError:
#             return redirect('add-email')
#         return redirect('add-email')
#     else:
#         print('leeres doc')
#         return redirect('add-email')

    