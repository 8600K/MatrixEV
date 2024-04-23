from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('responsible-gaming/', views.rg, name='responsible-gaming'),
    path('work-in-progress/', views.wip, name='work-in-progress'),
]
