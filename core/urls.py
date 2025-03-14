from django.urls import path

from core import views

urlpatterns = [
    path('', views.index, name='cea-homepage'),
    path('contact-us', views.show_contact_us, name='contact_us'),
    path('about-us', views.show_about, name='about_us'),

]
