from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

import time
import random
# Create your views here.
def main(request):
    '''
    Handles the request to go to the main.html page
    '''

    template_name = "resturant/main.html"
    
    return render(request, template_name)

def show_form(request):
    '''
    Handles the request to go to the order.html page
    '''
    template_name = "resturant/order.html"

    return render(request, template_name)

def submit(request):
    '''
    Process the form submission, and generate a result.
    '''
    #the current time
    current_time = time.localtime()

    #the pickup time to a random time 30-60 minutes from the current time
    minutes_until_pickup = random.randrange(30, 60)
    pickup_time = time.localtime(time.mktime(current_time) + (minutes_until_pickup * 60))

    template_name = "resturant/confirmation.html"

    if request.POST:
        name = request.POST['name']
        favorite_color = request.POST['favorite_color']
        context = {
            'name': name,
            'favorite_color':  favorite_color,
            #the current time
            'current_time': time.localtime(),
            #the pickup time to a random time 30-60 minutes from the current time
            'minutes_until_pickup': random.randrange(30, 60),
            'pickup_time': time.localtime(time.mktime(current_time) + (minutes_until_pickup * 60))
        }
    
        return render(request, template_name, context=context)


    return redirect("show_form")    

