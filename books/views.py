from django.shortcuts import redirect, render, get_object_or_404
from .models import *

# booksData = open('/home/nimrod/Django-project/books.json').read()
# data = json.loads(booksData)

def index(request):
    allBooks = Book.objects.all()
    context = {'books': allBooks }
    return render(request, 'books/index.html', context)

# Using the try-except to catch errors
# def show(request, id):
#     try:
#         singleBook = Book.objects.get(pk=id)
#     except Book.DoesNotExist:
#         raise Http404('Book Doesn\'t exist')
#     context = {'book': singleBook }
#     return render(request, 'books/show.html', context)

# ========== OR ============

# Using the get object or 404 method
def show(request, id):
    singleBook = get_object_or_404(Book, id=id)
    # Let's capture the reviews submitted for this book
    reviews = Review.objects.order_by('-posted')
    context = {'book': singleBook, 'reviews': reviews }
    return render(request, 'books/show.html', context)


def review(request):
    body = request.POST['review']
    newReview = Review(body=body)
    newReview.save()
    return redirect('/')