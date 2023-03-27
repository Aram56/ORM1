from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

def books_pagi(request, date):
    template = 'books/books_pagi.html'
    data = Book.objects.filter(pub_date=date).all()
    next_date = Book.objects.filter(pub_date__gt=date).order_by('pub_date').values_list('pub_date', flat=True).first()
    context = {'page': data,
               'next_page': next_date
               }
    return render(request, template, context)


    # value_date = request.Get.get('date')
    # list_date = []
    # data = Book.objects.filter(pub_date=date).all()
    # books = Book.objects.all().order_by('pub_date')
    # for book in books:
    #     list_date.append(book.pub_date)

    # previous_data = list_date.index('value_date') - 1
    # next_date_index = list_date.index(value_date) + 1
    # next_date = list_date[next_date_index]


    # context = {'page': data,
    #            'next_page': next_date, 
    #             'previous_page': previous_data
    #            }
    # return render(request, template, context)  


