from django.urls import path
from .import views
from .views import Prod_list, SearchResultsListView, Category_list
from .views import Prod_Details, Prod_Checkout

urlpatterns=[
    path('',Category_list.as_view(),name='cat_list'),
    path('list/<int:category_id>/',Prod_list.as_view(),name='list'),
    path('details/<int:pk>/',Prod_Details.as_view(),name = 'details'),
    path('search/',SearchResultsListView.as_view(),name='search'),
    path('checkout/<int:pk>/',Prod_Checkout.as_view(),name='checkout')
    

]


