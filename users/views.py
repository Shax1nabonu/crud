from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login , logout
# Create your views here.
def sign_up(request):
    if request.method =='POST':
        form=UserCreationForm(request. POST)
        print(form.is_valid())
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('article_func')
    form=UserCreationForm()
    return render(request, 'sign_up.html', {'form':form})

def sign_in(request):
    if request.method=='POST':
        form= AuthenticationForm(data=request. POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('article_func')
    form=AuthenticationForm()
    return render(request, 'sign_in.html', {'form':form})
    

def sign_out(request):
    logout(request)
    return redirect('sign_in')