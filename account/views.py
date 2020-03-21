from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('home')
    else:
      return render(request, 'account/login.html', {'error': '사용자 이름과 비밀번호를 확인해주세요.'})
  else:
    return render(request, 'account/login.html')

def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    confirm = request.POST['confirm']

    if username == "" or password == "" or confirm == "":
      return render(request, "account/signup.html", {'error': '폼을 모두 채워주세요.'})

    if password == confirm:
      user = User.objects.create_user(username, password=password)
      auth.login(request, user)
      return redirect('home')
    else:
      return render(request, "account/signup.html", {'error': '비밀번호를 다시 확인해주세요.'})
  return render(request, "account/signup.html")

def logout(request):
  auth.logout(request)
  return redirect('home')
