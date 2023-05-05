from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('book-trip/',views.book_trip,name='book_trip'),
]


