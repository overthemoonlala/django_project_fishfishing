from django.views.generic.base import TemplateView

class MainpageView(TemplateView):
   template_name = 'theme/main.html'
    
from django.shortcuts import render
from .models import Member
from django.http import HttpResponseRedirect



# Create your views here.

#로그인----------------------------------------------------------------------
def login(request):
    if request.method != 'POST':
        return render(request, 'member/login.html')
    else:
        # 파라미터값 저장
        id1 = request.POST["id"]
        pass1 = request.POST["pass"]
        try:
            member = Member.objects.get(id=id1)
            if member.pass1 == pass1 :
                session_id = request.session.session_key
                request.session['login'] = id1
                return HttpResponseRedirect("/index/")
            else:
                context = {"msg":"비밀번호가 틀립니다.","url":"../login/"}
                return render(request,'alert.html', context)
        except:
            context = {"msg":"아이디를 확인하세요."}
            return render(request,'member/login.html', context)
        
        

#회원가입--------------------------------------------------------------------
def join(request):
    if request.method != 'POST':
        return render(request, 'member/join.html')
    else:
        # 회원가입
        member = Member(id=request.POST['id'],\
                        pass1=request.POST['pass'],\
                        name=request.POST['name'],\
                        gender=request.POST['gender'],\
                        tel=request.POST['tel'],\
                        email=request.POST['email'],\
                        #picture=request.POST['picture']
                        )
        member.save()
        return HttpResponseRedirect("../login/")
    
    

#메인----------------------------------------------------------------------   
def main(request):
    return render(request, '../index.html')    
    
from django.contrib import auth    



#로그아웃--------------------------------------------------------------------
def logout(request) :
    auth.logout(request)
    return HttpResponseRedirect("http://localhost:8003/index/")   




    
#회원정보 수정--------------------------------------------------------------------
def update(request,id):
    try:
        login = request.session['login'] #세션정보.로그인 정보
    except:
        context={'msg': '로그인 하세요', 'url': '../../login/'}
        return render(request, 'alert.html', context)
    if login == id or login == 'admin' : #admin이거나 본인 아이디로 로그인 한 경우
        return update_rtn(request,id) # update_rtn
    else:
        context = {'msg': '본인정보만 수정가능합니다.','url':'/index/'}
        return render(request, 'alert.html', context)
    



def update_rtn(request, id):
    if request.method != 'POST' :
        member = Member.objects.get(id=id)
        return render(request, 'member/update.html', {"mem":member})
    else:
        member = Member.objects.get(id=id)
        if member.pass1 == request.POST['pass']:
            member = Member(id=request.POST['id'],\
                            name=request.POST['name'],\
                            pass1=request.POST['pass'],\
                            gender=request.POST['gender'],\
                            tel=request.POST['tel'],\
                            email=request.POST['email'],\
                           # picture=request.POST['picture']
                           )
            member.save()# id 존재하면 수정, id값 없으면 추가
            return HttpResponseRedirect("../../mypage/" + id + "/")
        #"../../info/" + id + "/"
        #"../../info"+ id +"/"
        # 짝대기 / 하나가 안들어갔음 => url매핑!!
        
        else:
            context = {"msg":"회원 정보 수정 실패. \\n비밀번호 오류입니다.", \
                           "url": "../../update/"+id+"/"}
            return render(request, 'alert.html', context)




#비밀번호 수정--------------------------------------------------------------------
def password(request,id):
    try:
        login = request.session['login'] #세션정보.로그인 정보
    except:
        context={'msg': '로그인 하세요', 'url': '../../login/'}
        return render(request, 'alert.html', context)
    
    if login == id :
        return password_rtn(request,id)
    else:
        context = {'msg': '본인정보만 수정가능합니다.','url':'../../main/'}
        return render(request, 'alert.html', context)
    


def password_rtn(request,id):
    if request.method != 'POST' :
        return render(request, 'member/passwordform.html', {"id":id})
    else:
        member = Member.objects.get(id=id)
        if member.pass1 == request.POST['pass']:
            member.pass1 = request.POST['chgpass']
            member.save()
            context = {"msg":"비밀번호 수정이 완료되었습니다.", \
                       "url":"../../mypage/" + id + "/", "closer":True}
            return render(request, 'member/password.html', context)
        else: #비밀번호 오류
            context = {"msg":"비밀번호 오류입니다.",\
                       "url":"../../password/"+id+"/","closer":False}
            return render(request, 'member/password.html', context)

#비밀번호 찾기-----------------------------------------------------------------


# 회원탈퇴--------------------------------------------------------------------
def delete(request,id):
    try:
        login = request.session['login'] #세션정보.로그인 정보
    except:
        context={'msg': '로그인 하세요', 'url': '../../login/'}
        return render(request, 'alert.html', context)    
    if login == id :
        return delete_rtn(request,id)
    else:
        context = {'msg': '3. 본인정보만 탈퇴가능합니다.','url':'/index/'}
        return render(request, 'alert.html', context)
    



def delete_rtn(request, id):
    if request.method != 'POST' :
        return render(request, 'member/delete.html', {"id":id})
    else:
        member = Member.objects.get(id=id)
        if member.pass1 == request.POST['pass']: # 비밀번호 일치
            member.delete() #db에서 삭제
            auth.logout(request) #세션종료. 로그아웃 상태
            context = {"msg":"회원님 탈퇴처리가 완료되었습니다.", \
                       "url":"/index/"}
            return render(request, 'alert.html', context)
        else: #비밀번호 오류
            context = {"msg":"비밀번호 오류입니다.", "url":"../../delete"+id+"/"}
            return render(request, 'alert.html', context)



#Mypage--------------------------------------------------------------------

def mypage(request,id):
    try:
        login = request.session["login"]
    except:
        login = ""
    
    if login != "":
        if login == id or login == 'admin':
            member = Member.objects.get(id=id)
            return render(request, "member/mypage.html",{"mem":member})
        else:
            context = {"msg":"본인정보만 조회 가능","url":"/index/"}
            return render(request,"alert.html", context)
    else:
        context = {"msg":"로그인하세요", "url":"../../login/"}
        return render(request,"alert.html",context)
    
    
#my_datalist-----------------------------------------------------------------
def my_datalist(request,id):
    try:
        login = request.session["login"]
    except:
        login = ""
    
    if login != "":
        if login == id or login == 'admin':
            member = Member.objects.get(id=id)
            return render(request, "member/my_datalist.html",{"mem":member})
        else:
            context = {"msg":"본인정보만 조회 가능","url":"/index/"}
            return render(request,"alert.html", context)
    else:
        context = {"msg":"로그인하세요", "url":"../../login/"}
        return render(request,"alert.html",context)    
