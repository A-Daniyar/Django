from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('function', views.hello_world),
    path('class', views.HelloView.as_view()),
    path('reservation', views.home),
]