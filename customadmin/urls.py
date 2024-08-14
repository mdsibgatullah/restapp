from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index.as_view(), name='customadmin'),
    path('booking/',views.Book.as_view(), name='booking'),
]