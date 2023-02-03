from django.shortcuts import render
from .models import Posts, Audio


def home(request):
    return render(request, 'jassong/home.html')


def resources(request):
    audious = Audio.objects.all()
    context = {"audious": audious}
    return render(request, 'jassong/resources.html', context)


def newsFeed(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'jassong/post.html', context)


def donation(request):
    return render(request, 'jassong/donation.html')


def mosque(request):
    return render(request, 'jassong/mosque.html')


def about(request):
    return render(request, 'jassong/about.html')


def contact(request):
    return render(request, 'jassong/contact.html')
