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
    context = {
        'current_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    }
    return render(request, template_name, context=context)

def show_form(request):
    '''
    Handles the request to go to the order.html page
    '''
    template_name = "resturant/order.html"

    specials = ['Soggy Wontons', 'Skeleton Soup', 'Chicken Fried Feet', 'Just a bowl']
    context = {
        'current_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        'special': random.choice(specials),
    }
    return render(request, template_name, context=context)

import time
import random
from django.shortcuts import render

def submit(request):
    '''
    Process the form submission and generate a confirmation.
    '''
    current_time = time.localtime()

    minutes_until_pickup = random.randrange(30, 60)
    pickup_time = time.localtime(time.mktime(current_time) + (minutes_until_pickup * 60))

    current_time_str = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    pickup_time_str = time.strftime("%Y-%m-%d %H:%M:%S", pickup_time)

    menu_items = {
        'Fried Wontons': 6.99,
        'Vegetable Soups': 7.99,
        'Chicken Fried Rice': 8.99,
        'Beef Lo Mein': 9.99,
        'Soggy Wontons': 10.99,
        'Skeleton Soup': 10.99,
        'Chicken Fried Feet': 10.99,
        'Just a bowl': 10.99,
    }

    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']

        items = request.POST.getlist('items')  
        special = request.POST.get('special')  
        special_instructions = request.POST.get('special_instructions', '')  

        if special:
            items.append(special)

        total = sum([menu_items[item] for item in items])
        context = {
            'name': name,
            'phone': phone,
            'email': email,
            'items': items,  
            'special_instructions': special_instructions,
            'total': total,

            'current_time': current_time_str,
            'pickup_time': pickup_time_str,
            'minutes_until_pickup': minutes_until_pickup,
        }

        template_name = "resturant/confirmation.html"
        return render(request, template_name, context=context)

    return redirect("show_form")    

