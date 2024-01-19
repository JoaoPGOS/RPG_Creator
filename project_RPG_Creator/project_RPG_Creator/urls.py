from django.urls import path
from app_RPG_Creator import views

urlpatterns = [
    # route, view, reference name
    path('cadpage',views.cadpage,name='cadpage'),
    path('cad_user',views.cad_user,name='cad_user'),
    path('homepage',views.homepage,name='homepage'),
    path('',views.loginpage,name='loginpage')
]
