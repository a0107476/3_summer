from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, login as django_login, logout as django_logout)
from django.contrib.auth.models import User
from auction.models import Write, Bid

def mymain(request):
    print(request.user.is_authenticated)
    try:
        if request.user.is_authenticated:
            print("1"*10)
            userdata = {
                "username" : request.user.username
                }
                
            loggeduser = request.user.username
            loggedid = request.user.id
            post = Write.objects.filter(writer = loggeduser) #내가 등록한 글
            post2 = Bid.objects.filter(userId_id = loggedid) #내가 입찰한 글
            print(post)
            print(post2)
            print('2'*10)
            context = {"userdata":userdata, "post":post, "post2":post2 }
            return render(request, "mypage/mymain.html", context)
        else:
            return redirect("/")

    except:
        return render(request, "mypage/error.html")

