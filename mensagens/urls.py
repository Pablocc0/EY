from django.urls import path

from . import views
#from .views import MensagemAPIView

urlpatterns = [
    path('', views.index),
]