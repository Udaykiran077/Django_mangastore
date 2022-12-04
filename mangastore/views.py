from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")
def uk(request):
    return render(request,"uk.html")
def register(request):
    return render(request,"register.html")    