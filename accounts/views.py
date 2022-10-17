from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import ResumeForm 
from .models import Resume
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

class HomeView(TemplateView):
    template_name = 'main/home.html'
    
    # @method_decorator(login_required)
    # def get_context_data(self, request, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        return render(request, self.template_name)

@method_decorator(login_required, name='dispatch')
class FormView(LoginRequiredMixin, View):
    form_class = ResumeForm
    initial = {'key': 'value'}
    template_name = 'accounts/resume.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse('File submitted')
    #     else:
    #         form = ResumeForm
    #     return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("File submitted") 
        else:
            form = ResumeForm
        return render(request, self.template_name, {'form':form})


class Profile(View):
    tempelate_name='accounts/profile.html'
    def post(self,request):
        profile_values = Resume.objects.all().values()
        context = {}
        data = []
        for i in profile_values:
            data.append(i)
        context['data'] = data
        return render(request, self.tempelate_name, context)
    
    def get(self,request):
        return render(request, self.tempelate_name)
    
class ResumeFormView(ListView):
    # specify the model to use
    model = Resume

class ResumeFormDelete(DeleteView):
    # specify the model you want to use
    model = Resume
    success_url ="/"
    