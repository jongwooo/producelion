from django.shortcuts import render
from vote.models import VoteList

def result(request):
    votes = VoteList.objects
    return render(request,'result/result.html',{'votes':votes})