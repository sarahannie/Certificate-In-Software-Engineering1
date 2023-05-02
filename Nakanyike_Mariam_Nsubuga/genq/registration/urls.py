
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register, name='register'),
    path('new',views.new,name='new'),
    path('reg',views.reg, name="reg"),
    path('myForm/', views.display, name='myForm'),   # URL for the form view
    path('display/<str:firstname>/<str:lastname>/<int:gender>/<str:country>/<str:town>/<str:num1>/<str:state>/<str:email>/<str:date>/', views.display, name='display'),
    path('display/', views.display, name='display'),
    path('forms',views.aboutForm,name="forms"),
]