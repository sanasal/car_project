from django.shortcuts import render , redirect
from advertisment.models import *
from product.models import *
from django.http import JsonResponse , HttpResponseBadRequest 
import json  
from .forms import *
from django.http import JsonResponse
from django.http import HttpResponseNotFound
import urllib
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm
from user.models import Userinfo, Country
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from user.models import User  # your custom User model
from uuid import UUID
from product.models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate ,  get_user_model
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

User = get_user_model()

def home(request):
    cars = Advertisment.objects.all()

    context = {
        'cars': cars,
        'manufacturers': Manufacturer.objects.filter(is_deleted=False),
        'models': CarModel.objects.filter(is_deleted=False),
        'colors': Color.objects.filter(is_deleted=False),
    }
    return render(request, "home.html", context)




def cars_filter_view(request):
    cars = Product.objects.filter(is_deleted=False, is_sold=False)

    manufacturer_id = request.GET.get('manufacturer')
    manufacturer_location = request.GET.get('manufacturer_location')
    model_id = request.GET.get('model')
    color_id = request.GET.get('color')

    try:
        if manufacturer_id:
            cars = cars.filter(carModel__manufacturer__id=UUID(manufacturer_id))
        if manufacturer_location:
            cars = cars.filter(carModel__manufacturer__location__iexact=manufacturer_location)
        if model_id:
            cars = cars.filter(carModel__id=UUID(model_id))
        if color_id:
            cars = cars.filter(color__id=UUID(color_id))
    except:
        pass

    return render(request, 'cars_filter.html', {'cars': cars})


def contact_us(request):
    '''Display the contact us page'''

    return render(request,'contact_us.html')

def send_contact(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            # Save to database
            contact_request = form.save()
            
             # Send to WhatsApp
            phone_number = "963938173371"   
            message = (
                f"Name: {contact_request.name}\n"
                f"Email: {contact_request.email}\n"
                f"Subject: {contact_request.subject}\n"
                f"Message: {contact_request.message}\n"
            ) 
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

            return redirect(whatsapp_url)

        else:
            cars = Product.objects.all()
            return render(request, 'cotact_us.html', {'cars': cars, 'form': form})

    return redirect('frontend:contact_us')


def service(request):
    '''Display the services page'''

    return render(request , 'service.html')

def about(request):
    '''Display the about page'''

    return render(request , 'about.html')

def financing(request):
    '''Display the financing page'''
    cars = Product.objects.all()
    form = RequestsForm()

    context = {
        'cars': cars,
        'form': form,
    }

    if request.method == 'POST':
        try:
            body = json.loads(request.body) if request.content_type == 'application/json' else request.POST

            car_price = float(body.get('car_price', 0))
            downpayment = float(body.get('downpayment', 0))
            loan_duration = int(body.get('loan_duration', 1))
            action = body.get('action', "")  

            monthly_interest = ((car_price * 4)/100) / 12
            total_price = car_price + (monthly_interest*loan_duration)
            estimated_monthly_payment = (total_price - downpayment) / loan_duration

            return JsonResponse({
                'estimated_monthly_payment': f"SYP {estimated_monthly_payment:.2f}",
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    elif request.method == 'GET':
        return render(request, "financing.html" , context)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def send_financing_request_data(request):
    if request.method == 'POST':

        form = RequestsForm(request.POST)

        if form.is_valid():
            # Save to database
            financing_request = form.save()
            
             # Send to WhatsApp
            phone_number = "963938173371"   
            message = (
                f"Car: {financing_request.car}\n"
                f"Name: {financing_request.name}\n"
                f"Phone: {financing_request.mobile_phone}\n"
                f"Payment Method: {financing_request.payment_method}\n"
                f"Language: {financing_request.language}\n"
            ) 
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

            return redirect(whatsapp_url)

        else:
            cars = Product.objects.all()
            return render(request, 'financing.html', {'cars': cars, 'form': form})

    return redirect('frontend:financing')

def car_detail(request , car_id):
    '''Display the Car details page'''
    car = Product.objects.get(id = car_id)

    context = {
        'car':car,    
    }

    return render(request , 'detail.html' , context)

def FAQs(request):
    '''Display the services page'''

    return render(request , 'FAQs.html')

def team(request):
    '''Display the about page'''

    return render(request , 'team.html')

def cars(request):
    '''Display the home page'''
    cars = Product.objects.all()

    context = {
        'cars':cars,
        'manufacturers': Manufacturer.objects.filter(is_deleted=False),
        'models': CarModel.objects.filter(is_deleted=False),
        'colors': Color.objects.filter(is_deleted=False),
    }

    return render(request, 'car.html',context)


def testimonial(request):
    '''Display the contact us page'''

    return render(request , 'testimonial.html')

def sign_in(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontend:home')
    else:
        form = UserRegisterForm()
    return render(request, 'sign_in.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('frontend:home')
    else:
        form = UserLoginForm()
    return render(request, 'log_in.html', {'form': form})


def log_out(request):
    '''Go outside the website'''
    if request.method == 'POST':
        logout(request)   
        return redirect ('frontend:home')
