from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^verify$', views.verify),
    url(r'^books$', views.books), 
    url(r'^login$', views.login),
    url(r'^books/add$', views.add_review), 
    url(r'^process/review$', views.process_review),
    url(r'^process/reviewtwo(?P<number>\d+)$', views.process_review2),
    url(r'^book_page(?P<number>\d+)$', views.book_page), 
    url(r'^user_page(?P<number>\d+)$', views.users_page), 
    url(r'^delete(?P<number>\d+)$', views.delete),
    url(r'^logout$', views.logout),
       
]