from django.shortcuts import render
from account.models import Profile
from .models import VoteList
from django.contrib.auth.models import User
def vote(request):
  picks = Profile.objects
  return render(request, "vote/list.html",{'picks':picks})

def complete(request):
  myvote = VoteList()
  myvote.user = request.user
  myvote.myname = request.user.username
  myvote.name = request.POST.get('pick')
  myvote.save()
  return render(request,"vote/complete.html")
