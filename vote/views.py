from django.shortcuts import render,redirect
from account.models import Profile
from .models import VoteList
from django.contrib.auth.models import User

def vote(request):
  picks = Profile.objects.all()
  if not picks:
    return render(request, "vote/nolist.html")
  else:
    return render(request, "vote/list.html",{'picks':picks})

def complete(request):
    nowuser = VoteList.objects.filter(user=request.user)
    if not nowuser:
      myvote = VoteList()
      myvote.user = request.user
      myvote.myname = request.user.username
      myvote.team = request.POST.get('pick')
      myvote.votenum += 1
      myvote.save()
    else:
      obj = VoteList.objects.get(user = request.user)
      if obj.lastteam == request.POST.get('pick'):
        return render(request,"vote/error.html")
      else:
        obj.team = request.POST.get('pick')
        obj.votenum += 1
        obj.save()
    return render(request,"vote/complete.html")
