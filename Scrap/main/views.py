from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def home_view(request: HttpRequest):

    return render(request, "main/index.html")



def form_example(request: HttpRequest):

    return render(request, "main/form_example.html")



def content_example(request: HttpRequest):

    return render(request, "main/content_example.html")
