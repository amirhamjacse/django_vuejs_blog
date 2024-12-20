from django.contrib import admin
from django.urls import path
from blogmanage import views


urlpatterns = [
    path('list/', views.BlogList.as_view(), name='list'),
    path('create/<int:category_id>/', views.BlogCreateView.as_view(), name='blog-create'),
    path('details/<int:id>/', views.BlogRetriveView.as_view(), name='details'),
    path('update/<int:id>/', views.BlogUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', views.DestroyView.as_view(), name='delete'),
    path('category/list/', views.CategoryList.as_view(), name='category-list'),
]
