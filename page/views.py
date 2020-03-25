from django.shortcuts import render
from vote.models import VoteList
from vote.urls import urlpatterns
# Create your views here.

def home(request):
  if(VoteList.user==None):
    return render(request, "home.html")
  else:
    return render(request,"completion.html")
