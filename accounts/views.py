from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .form import UserForm, LoginForm

class UserFormView(View):
    form_class = UserForm
    template_name = 'accounts/registration_form.html'

    #display Blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)

            # Cleaned(Normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user if credentials are currect
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
        return render(request, self.template_name, {'form' : form})

class UserLogin(View):
    template_name = 'accounts/login_form.html'

    #display Blank form
    def get(self, request):
        form = LoginForm(None)
        return render(request, self.template_name, {'form' : form})

    #process form data
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():

            # Cleaned(Normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #returns user if credentials are currect
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('music:index')

        return render(request, self.template_name, {'form' : form})
