from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from django.core.mail import send_mail


# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-id')
    context = {'posts': posts, }
    return render(request, 'home.html', context)


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        message = 'Name: ' + message_name + '\n' + 'Email: ' + message_email + '\n' + 'Message: ' + message

        # send an email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            [''], # to email
        )
        return render(request, 'contact.html', {'message_name': message_name, 'message_email': message_email, 'message': message})
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})