from django.shortcuts import render

# Create your views here.
def app_home(request):
    return render(request, 'app.html')

def blog(request):
    return render(request, 'blog.html')