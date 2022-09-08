from django.urls import path
from . import views


'''
http://localhost:8003/analysis/xxxxx/
'''
urlpatterns = [
    path('picture/',views.picture,name='picture'),
    path('result/',views.result,name='result'),
    ]