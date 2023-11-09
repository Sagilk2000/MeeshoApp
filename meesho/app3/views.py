from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Products, category


# Create your views here.
class Category_list(ListView):
    model = category
    template_name = 'cat_list.html' 
    
    
    
    
class Prod_list(ListView):
    model = Products
    template_name = 'productlist.html'
    context_object_name = 'products'

    
    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id is not None:
            return Products.objects.filter(categories_id=category_id)
        else:
            return Products.objects.all()
    
    

class Prod_Details(DetailView):
    model = Products
    context_object_name = 'list'
    template_name = 'productdetails.html'

class SearchResultsListView(ListView):
    model = Products
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Products.objects.filter(
            Q(title=query)
        )

class Prod_Checkout(DetailView):
    model = Products
    template_name = 'checkout.html'


def PaymentComplete(request, pk):
    product = Products.object.get(id=pk)
    product.object.create(
        product=product
    )


    