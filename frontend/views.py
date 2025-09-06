from django.shortcuts import render

# Create your views here.

def home(request):
    '''Display the home page'''

    return render(request, 'home.html')


def contact_us(request):
    '''Display the contact us page'''

    return render(request , 'contact_us.html')

def service(request):
    '''Display the services page'''

    return render(request , 'service.html')

def about(request):
    '''Display the about page'''

    return render(request , 'about.html')

def financing(request):
    '''Display the home page'''

    return render(request, 'financing.html')

def car_detail(request):
    '''Display the contact us page'''

    return render(request , 'detail.html')

def FAQs(request):
    '''Display the services page'''

    return render(request , 'FAQs.html')

def team(request):
    '''Display the about page'''

    return render(request , 'team.html')

def cars(request):
    '''Display the home page'''

    return render(request, 'car.html')


def testimonial(request):
    '''Display the contact us page'''

    return render(request , 'testimonial.html')

