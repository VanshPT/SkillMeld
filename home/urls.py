from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('fillForm/', views.fillForm, name="Fill Form")
]