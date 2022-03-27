from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-id')
    context = {'posts': posts, }
    return render(request, 'home.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        #send Email
        send_mail(
            #subject
            'New Message from ' + name,
            #message
            message,
            #from Email
            email,
            #to Email
            ['karanironny25@gmail.com'],
        )
        
        messages.success(request, 'Your message has been sent!')
        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})