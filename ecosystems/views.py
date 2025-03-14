from django.shortcuts import render


# Create your views here.
def show_ecosystems(request):
    return render(request, 'ecosystems.html')
