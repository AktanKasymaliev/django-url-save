from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from urlapp.forms.auth import SignUpForm
from urlapp.forms.auth import LogInForm

User = get_user_model()

class SignUpView(generic.CreateView):
    template_name = 'auth/signup.html'
    form_class = SignUpForm
    model = User

    def post(self, request):
        post_request = super().post(request)
        if post_request.status_code == 302:
            user = authenticate(
                request,
                username=request.POST.get('username'),
                password=request.POST.get('password'),
            )
            login(request, user)
        return post_request 

    def get_success_url(self) -> str:
        return reverse('home')

class LogInView(generic.View):

    template_name = 'auth/login.html'
    form_class = LogInForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=request.POST.get('username'),
                password=request.POST.get('password'),
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})
        

class LogOutView(generic.View):
    
    def get(self, request):
        logout(request)
        return redirect('home')