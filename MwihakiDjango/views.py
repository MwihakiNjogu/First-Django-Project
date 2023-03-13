from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')
def services(request):
    return render(request, 'services.html')

def product(request):
    return render(request,'products.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'about.html')

def indexpage(request):
     return render(request,'index.html')