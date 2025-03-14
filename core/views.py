from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'homepage.html')


def show_contact_us(request):
    return render(request, 'contact_us.html')


def show_about(request):
    return render(request, 'about_us.html')
