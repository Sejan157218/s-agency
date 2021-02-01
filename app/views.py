from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from app.models import Contact
from app.models import Team
from app.models import Admin
from app.models import Frontadmin
from app.models import Portfolio
from app.models import Service
from app.models import Blog
from app.models import Testomonial

from datetime import datetime

# Create your views here.
def index(request):
    testomonial = Testomonial.objects.all()
    blog = Blog.objects.all()
    services = Service.objects.all()
    frontadmins = Frontadmin.objects.all()
    context = {'frontadmins':frontadmins,'services':services,'blog':blog,'testomonial':testomonial}
    return render(request,"index.html",context)

def about(request):
    testomonial = Testomonial.objects.all()
    admins = Admin.objects.all()
    teams = Team.objects.all()
    context = {'admins':admins,'teams':teams,'testomonial':testomonial}
    
    return render(request,'about.html',context)

def services(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request,'services.html',context)

def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {'portfolios':portfolios}
    return render(request,'portfolio.html',context)

def blog_details(request):
    return render(request,'blog_details.html')

def contact(request):
    if request.method == "POST":
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']

        contact = Contact(name=name, email=email, phone=phone, message=message,subject=subject, date=datetime.today())
        contact.save()
        
        #send email
        send_mail(subject, "Full Name : " + name +"\n"  + "Email : "+ email+ "\n" +"Mobile : "+ phone +"\n" + "\n" +"Message : " + message,"sejan3515@gmail.com",["sejan157218@gmail.com"],fail_silently=False,)


        return render(request, 'contact.html',{'name': name} )
    else:
        return render(request, 'contact.html', {})
