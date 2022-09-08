from django.urls import path
from . import views


'''
http://localhost:8003/fishlist/xxxxx/
'''
urlpatterns = [
    path('list/',views.list,name='list'),
    #path('detail/<int:id>/',views.detail,name='detail'),
    ]
