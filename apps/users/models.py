from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255) 
    alias = models.CharField(max_length=255, null = True)   
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User object: {} {} {} {} {}>".format(self.first_name, self.last_name, self.alias, self.email, self.password)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Author object: {} {}>".format(self.first_name, self.last_name)

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Book object: {} {}>".format(self.name, self.author)

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField(null = True)
    user = models.ForeignKey(User, related_name="reviews_posted")
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Review object: {} {} {} {}>".format(self.review, self.rating, self.user, self.book)



