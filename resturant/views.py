from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.
def main(request):
    '''
    Handles the request to go to the main.html page
    '''

    template_name = "resturant/main.html"
    
    return render(request, template_name)