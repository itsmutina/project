from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
    path('earn/',views.earn, name = 'earn'),

    path('withdraw/', views.withdraw, name = 'withdraw'),
    path('confimation/', views.withdrawconfirm, name = 'confirmation'),

    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.registerPage, name = 'register'),

    path('<str:ref_code>/', views.home, name = 'home'),



]