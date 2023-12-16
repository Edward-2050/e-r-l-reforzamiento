from django.urls import path
from . import views

urlpatterns = [
    path('archivo/', views.archivo_cat, name='archivo_cat')
]
