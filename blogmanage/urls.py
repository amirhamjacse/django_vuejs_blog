from django.contrib import admin
from django.urls import path
from blogmanage import views

urlpatterns = [
    path('list/', views.BlogList.as_view(), name='list'),
]
