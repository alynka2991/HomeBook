"""HomeBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('measures/', views.MeasureListView.as_view(), name='measures'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category-update'),
    path('measure/<int:pk>', views.MeasureDetailView.as_view(), name='measure-detail'),
    path('measure/<int:pk>/update/', views.MeasureUpdate.as_view(), name='measure-update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category-delete'),
    path('measure/<int:pk>/delete/', views.MeasureDelete.as_view(), name='measure-delete'),
    path('category/create/', views.CategoryCreate.as_view(), name='category-create'),
    path('measure/create/', views.MeasureCreate.as_view(), name='measure-create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),
]
