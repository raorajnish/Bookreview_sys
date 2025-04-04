from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.views import View
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def home(request):
    return render(request, 'base.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all()
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})

@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('app:book_detail', book_id=book.id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'book': book, 'form': form})

