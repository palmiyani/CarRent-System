from django.urls import path
from . import views


urlpatterns =[
    path('',views.index),
    path('services/',views.services),
    path('cars/',views.cars),
    path('about/',views.about),
    path('contact/',views.contact),
    path('login/',views.logindemo),
    path('registration/',views.registration),
    path('Logout/',views.Logout),
]