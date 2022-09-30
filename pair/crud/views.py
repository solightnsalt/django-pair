from django.shortcuts import render, redirect
from .models import Review
import datetime

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "crud/index.html", context)


def create(request):
    return render(request, "crud/create.html")


def created_at(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    Review.objects.create(
        title=title,
        content=content,
    )
    return redirect("crud:index")


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        "review": review,
    }
    return render(request, "crud/detail.html", context)


def delete(request, review_pk):
    Review.objects.get(pk=review_pk).delete()
    return redirect("crud:index")


def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        "review": review,
    }
    return render(request, "crud/update.html", context)


def updated(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    title_updated = request.GET.get("title_updated")
    content_updated = request.GET.get("content_updated")
    review.title = title_updated
    review.content = content_updated
    review.save()
    return redirect("crud:index")
