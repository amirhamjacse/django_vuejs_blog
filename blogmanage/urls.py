from django.contrib import admin
from django.urls import path
from blogmanage import views

urlpatterns = [
    path('list/', views.BlogList.as_view(), name='list'),
    path('details/<int:pk>', views.BlogRetriveView.as_view(), name='details'),
    path('create/', views.BlogCreateView.as_view(), name='create'),
]
