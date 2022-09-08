from django.urls import path

from .views import *
from . import views
#추가


urlpatterns = [
    path('index/', MainpageView.as_view(), name='mainpage'),
    path('login/', views.login,name='login'),
    path('join/', views.join,name='join'),
    path('logout/',views.logout,name='logout'),
    path('update/<str:id>/',views.update,name='update'), 
    path('delete/<str:id>/',views.delete,name='delete'),
    path('password/<str:id>/',views.password,name='password'),
    path('mypage/<str:id>/',views.mypage,name='mypage'),
    path('my_datalist/<str:id>/',views.my_datalist,name='my_datalist'),
#추가

    ]
