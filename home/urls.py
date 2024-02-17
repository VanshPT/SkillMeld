from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('fillForm/', views.fillForm, name="Fill Form"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]