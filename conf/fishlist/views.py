from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Nomal, Poison, Extinct

# https://lsjsj92.tistory.com/480


# ▶ 리스트
def list(request):
    if request.method != "POST":
        fish = '1'
#        return render(request, 'fishlist/list.html')
    else:
        fish = request.POST.get("fish",'1')
        
    if fish == '1': #일반어류
        nomallist = Nomal.objects.all()
        return render(request, 'fishlist/list.html', {"nomallist": nomallist})
    elif fish == '2' : #독성어류
        poisonlist = Poison.objects.all()
        return render(request, 'fishlist/list.html', {'poisonlist' : poisonlist})
    elif fish == '3' : #멸종위기어류
        extinctlist = Extinct.objects.all()
        return render(request, 'fishlist/list.html', {'extinctlist': extinctlist})
          
       
       
           
       
    
    
