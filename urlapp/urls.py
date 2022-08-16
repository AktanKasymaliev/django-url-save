from django.urls import path

from urlapp.views import url_logic
from urlapp.views import auth

urlpatterns = [
    #url-logic
    path('', url_logic.HomeView.as_view(), name='home'),

    #auth
    path('signup/', auth.SignUpView.as_view(), name='signup'),
    path('login/', auth.LogInView.as_view(), name='login'),
    path('logout/', auth.LogOutView.as_view(), name='logout'),
]