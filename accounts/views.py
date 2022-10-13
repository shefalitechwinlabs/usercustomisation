from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import ResumeForm 
from .models import *

def resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponse("File submitted") 
    else:
        form = ResumeForm
    return render(request, 'resume.html', {'form':form})

def profile(request):
    profile_values = Resume.objects.all().values()
    context = {}
    data = []
    for i in profile_values:
        data.append(i)
    context['data'] = data
    return render(request, 'profile.html', context)
    