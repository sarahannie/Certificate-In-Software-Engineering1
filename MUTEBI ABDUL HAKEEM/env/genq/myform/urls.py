from django.urls import path
from myform import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('index/', views.home, name = 'index'),
    path('home/', views.index, name = 'home'),
    path('', auth_views.LoginView.as_view(template_name = 'products/login.html'), name = 'login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'products/logout.html'), name = 'logout' ),
    path('myForm/', views.display, name='myForm'),   # URL for the form view
    path('display/<str:firstname>/<str:lastname>/<int:gender>/<str:country>/<str:town>/<str:num1>/<str:state>/<str:email>/<str:date>/', views.display, name='display'),
    path('display/', views.display, name='display')
]

