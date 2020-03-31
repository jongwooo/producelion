from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.vote, name='vote'),
    path('complete',views.complete,name='complete'),
]
