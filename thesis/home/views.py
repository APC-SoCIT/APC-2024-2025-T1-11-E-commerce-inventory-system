from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def preorder(request):
    return render(request, 'home/preorder.html')

def profile(request):
    return render(request, 'home/profile.html')

def logout_view(request):
    # Implement logout functionality
    pass

def create(request):
    return render(request, 'home/create.html')