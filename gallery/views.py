from django.shortcuts import render
from django.utils import timezone
from .models import Photo

def photo_list(request):
    photos = Photo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'gallery/photo_list.html', {'photos': photos})
