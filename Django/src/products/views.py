from django.shortcuts import render

from .forms import ProductForm, RawProductFrom

from .models import Product
# Create your views here.
def product_create_view(request):
    my_form = RawProductFrom()
    context = {
        "form": my_form
    }
    return render(request, 'products/product_create.html', context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm(request.POST or None)
#     context = {
#         'form': form
#     }
#     return render(request, 'products/product_create.html', context)

# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     my_title = request.POST.get('title')
#     print(my_title)
#     # Product.objects.create(title = my_title)
#     context = {}
#     return render(request, 'products/product_create.html', context)

def product_detail_view(request):
    obj = Product.objects.get(id=2)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, 'products/product_create.html', context)