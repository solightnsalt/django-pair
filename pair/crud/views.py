from django.shortcuts import render, redirect
from .models import Review

# Create your views here.


def index(request):

    return render(request, "crud/index.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    Review.objects.create(title=title, content=content)
    return render(request, "crud/create.html")


def detail(request, pk):
    reviews = Review.objects.get(pk=pk)
    context = {
        "reviews": reviews,
    }
    return render(request, "crud/detail.html", context)
