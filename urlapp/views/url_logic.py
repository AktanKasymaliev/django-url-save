from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from urlapp.forms.url_logic import LinksCreateForm
from urlapp.models import Link

class HomeView(LoginRequiredMixin, View):

    template_name = 'pages/home.html'
    form_class = LinksCreateForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})
        
    def post(self, request):
        form = self.form_class(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, self.template_name, context={'form': form})

class MyLinksView(LoginRequiredMixin, View):
    template_name = 'pages/mylinks.html'

    def get(self, request):
        my_links = Link.objects.filter(user=request.user)
        return render(
            request, 
            self.template_name, 
            {"links": my_links}
            )

class SeeMyLinksView(LoginRequiredMixin, View):
    template_name = 'pages/detail_links.html'

    def get(self, request, pk):
        link_group = get_object_or_404(Link, pk=pk)
        return render(
            request,
            self.template_name,
            {
            "link": link_group,
            "urls": link_group.url.split('\r\n')
            }
        )