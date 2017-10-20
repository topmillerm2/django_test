from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
from django.contrib.messages import constants as message_constants
import bcrypt
import datetime


def index(request):
    # user = request.session['id']
    # author = request.POST['new_author']
    # new_book = Book.objects.create(name = request.POST['title'], author = author)
    # new_review = Review.objects.create(review = request.POST['review'], rating = request.POST['rating'], user = user, book = new_book)
    # context = {
    #     "new_book": new_book,
    #     "new_review": new_review
    # }
    return render(request, 'users/index.html')

def verify(request):
    if len(request.POST['first_name']) == 0 or len(request.POST['last_name']) == 0 or len(request.POST['alias']) == 0 or len(request.POST['email']) == 0 or len(request.POST['password']) == 0:
        messages.error(request, 'All fields must be filled out!')
        return redirect ('/')
    if not request.POST['first_name'].isalpha() or not request.POST['last_name'].isalpha():
        messages.error(request,'First and Last names can only contain letters!')
        return redirect ('/')
    if request.POST['password'] != request.POST['confirm_pw']:
        messages.error(request,'Passwords must match!')
        return redirect ('/')
    if request.POST['password'] < 8:
        messages.error(request,'Passwords must be at least 8 characters long!')
        return redirect ('/')

    password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    new_user = User.objects.create(first_name= request.POST['first_name'], last_name = request.POST['last_name'], alias = request.POST['alias'], email = request.POST['email'], password = password_hash)
    request.session['id'] = new_user.id
    request.session['name'] = new_user.first_name
    return redirect('/books')

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if len(user) > 0:
        user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            return redirect('/books')
        else:
            messages.error(request, 'Email/Password invalid')
            return redirect('/')
    else:
        messages.warning(request, 'User not found')
    # if len(request.POST['email']) == 0 or len(request.POST['password']) == 0:
    #     messages.error(request, 'All fields must be filled out!')
    #     return redirect ('/')  
    return redirect('/')  

def books(request):
    reviews = Review.objects.order_by('-id')[:3]
    books = Book.objects.all()
    context = {
        "reviews": reviews,
        "books": books
    }
    return render(request, 'users/books.html', context)

def add_review(request):
    
    return render(request, 'users/add_book.html')

def process_review(request):
    user = User.objects.get(id =request.session['id'])
    author = Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'])
    new_book = Book.objects.create(name = request.POST['title'], author = author)
    new_review = Review.objects.create(review = request.POST['review'], rating = request.POST['rating'], user = user, book = new_book)
    return redirect('/book_page{}'.format(new_book.id))

def process_review2(request, number):
    user = User.objects.get(id =request.session['id'])
    book = Book.objects.get(id = number)
    new_review = Review.objects.create(review = request.POST['review'], rating = request.POST['rating'], user = user, book = book)
    return redirect('/book_page{}'.format(number))

def book_page(request, number):
    book_id = Book.objects.filter(id = number)
    new_book = Book.objects.filter(id = number)
    new_review = Review.objects.filter(book = new_book)
    context ={
        "new_book": new_book,
        "new_review": new_review,
        "book_id": book_id
    }
    return render (request, 'users/book_page.html', context)

def users_page(request, number):
    user = User.objects.filter(id =number)
    reviews = Review.objects.filter(user = user)
    review_count = len(reviews)
    context = {
        "user": user,
        "reviews": reviews,
        "review_count": review_count,
    }
    return render (request, 'users/user_page.html', context)

def delete(request, number):
    Review.objects.get(id = request.POST['review_id']).delete()
    return redirect('/book_page{}'.format(number))

def logout(request):
    del request.session
    return redirect('/')




