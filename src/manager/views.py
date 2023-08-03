from django.shortcuts import render
from django.views import View

from manager.models import Book


# Create your views here.
class BookView(View):
    def get(self, request):
        data = {"books" : Book.objects.all()}
        return render(request, "index.html", context=data)

class AddLike(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        book.likes +=1

