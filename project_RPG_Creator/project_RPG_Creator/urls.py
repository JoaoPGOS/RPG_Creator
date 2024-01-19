from django.urls import path
from app_RPG_Creator import views

urlpatterns = [
    # route, view, reference name
    path('forgotpassword',views.forgot_password,name='forgot_password'),
    path('recoverpassword',views.request_to_recover_password, name='change_password'),

    path('cadpage',views.cadpage,name='cadpage'),
    path('caduser',views.cad_user,name='cad_user'),
    path('endverification',views.end_verification,name='end_verification'),

    path('homepage',views.homepage,name='homepage'),
    path('',views.loginpage,name='loginpage')
]
