from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from django.contrib.auth import authenticate, login

class LoginView(View):
    template_name = 'authentication/login.html'

    def post(self, request):
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                request.session['username'] = username
                return redirect('/home')
            else:
                context = {'error': 'Username or password is incorrect!'}
                return render(request, 'authentication/login.html', context)

        if "username" in request.session:
            return redirect('home/')
        else:
            return render(request, 'authentication/login.html')

    def get(self, request):
        template_name='authentication/login.html'
        return render(request, self.template_name)

class LogoutView(View):
    template_name='authentication/logout.html'
    def get(self, request):
        auth.logout(request)
        username = request.session.get('username')
        del username
        return render(request, self.template_name)