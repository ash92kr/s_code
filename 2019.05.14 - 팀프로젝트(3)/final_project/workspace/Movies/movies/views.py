from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'movies/list.html')
    
def contact(request):
    return render(request, 'movies/contact.html')
    
def about(request):
    return render(request, 'movies/about.html')
    
    