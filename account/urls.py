from django.urls import path
from . import views

urlpatterns = [
    path("", views.account, name = "account"),
    path('form/', views.form, name = 'form'),
     path('register/', views.register, name = 'register')
]
