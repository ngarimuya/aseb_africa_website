from django.urls import path

from ecosystems import views

urlpatterns = [
    path('ecosystems', views.show_ecosystems, name='ecosystems'),

]
