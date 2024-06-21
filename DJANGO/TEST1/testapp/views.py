from django.shortcuts import render,redirect
from .forms import registerform
from .models import Users
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
# Create your views here.
def signup(request):
    form=registerform
    if request.method=="POST":
        form = registerform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            confirmpassword=form.cleaned_data['confirmpassword']
            print(password,username,confirmpassword)
            if password == confirmpassword:
                form.username=username
                form.password=password
                form.confirmpasswordpassword=confirmpassword
                form.save()
                return redirect('signin')
            else:
                print('password doesnt match')
                form.add_error('confirmpassword', "Passwords do not match.")
                form=registerform()
            

    return render(request,'signup.html',{'form':form})
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        if username and password:
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse('successs')
            print(user)
    else:
        return redirect ('signin')
    return render(request,'signin.html')