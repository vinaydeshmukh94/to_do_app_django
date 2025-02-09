from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from to_do import models
from to_do.models import TODOO
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')

        my_user = User.objects.create_user(username=fnm, 
                                           email=emailid, 
                                           password=pwd)
        my_user.save()

        print(f'fname - {fnm}, pwd-{pwd}, emailid-{emailid}')
        return render(request, 'login.html') # redirect to login page

    return render(request, 'signup.html') 


def loginn(request):
    if request.method == "POST":
        fnm = request.POST.get('fnm') 
        pwd = request.POST.get('pwd')

        print(fnm, pwd)

        userr = authenticate(request=request, username=fnm, password=pwd)

        if userr is not None:
            login(request=request, 
                  user=userr)
            return redirect('/todopage')
        else:
            return redirect('/login')

    return render(request, 'login.html')


@login_required(login_url='/login')
def todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        print(title)
        obj=models.TODOO(title=title, user=request.user)
        obj.save()

        res = models.TODOO.objects.filter(user=request.user).order_by('-date')
        return redirect('/todopage', {'res':res})
    login_required(login_url='/login')
    res = models.TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res':res })


@login_required(login_url='/login')
def edit_todo(request, srno):
    if request.method == "POST":
        title = request.POST.get('title')
        print(title)

        obj=models.TODOO.objects.get(srno=srno)
        obj.title = title
        obj.save()

        return redirect('/todopage', {'obj':obj})
    
    obj=models.TODOO.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj':obj })


@login_required(login_url='/login')
def delete_todo(request, srno):
    obj=models.TODOO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')


def signout(request):
    logout(request=request)
    return redirect('/login')
