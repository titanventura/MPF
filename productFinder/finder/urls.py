from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns=[
    path('',views.index,name="index"),
    path('About/',views.about,name="about"),
    path('Product_Create/',views.reviewers,name="revform"),
    path('Brand_Create/',views.branders,name="brandform"),
    path('Prod_List/',views.ProdLsView.as_view(),name="ProdList"),
    path('Brand_list/',views.BrandListView.as_view(),name="BrandList"),
]