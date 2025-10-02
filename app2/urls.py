from django.urls import path
from . import views


urlpatterns =[
    path('',views.index1),
    path('services1/',views.services1),
    path('cars1/',views.cars1),
    path('about1/',views.about1),
    path('contact1/',views.contact1),
    path('login1/',views.login1),
    path('registration1/',views.registration1),
    path('Logout1/',views.Logout1),
    path('application/',views.application),
]

