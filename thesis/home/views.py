from django.shortcuts import render
from inventory.models import Product

def home(request):
    return render(request, 'home/home.html')

def preorder(request):
    products = Product.objects.all()
    if request.method == 'POST':
        # Handle form submission
        product_id = request.POST.get('product')
        customer_name = request.POST.get('customer_name')
        quantity = request.POST.get('quantity')
        # Save the order (you need to define the Order model and save the order here)
        # ...
    return render(request, 'home/preorder.html', {'products': products})

def profile(request):
    return render(request, 'home/profile.html')

def logout_view(request):
    # Implement logout functionality
    pass

def create(request):
    return render(request, 'home/create.html')