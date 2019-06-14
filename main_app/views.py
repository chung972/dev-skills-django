from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# from django.contrib.auth.decorators import login_required
# not using the above decoratr because we don't have any view functiosn that we want to restrict visitors from
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import LoginForm
from . models import Skill

# Create your views here.


def home(request):
    return render(request, 'home.html')
    # like how render behaves in express, render in django also looks for
    # files RELATIVE to the templates directory


def signup(request):
    # need to refactor to post form to db
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def login_view(request):
    err_msg = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate the User
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                err_msg = 'Sorry, your username or password was invalid.'
    form = LoginForm()
    context = {
        'form': form,
        'err_msg': err_msg,
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


class CreateSkill(LoginRequiredMixin, CreateView):
    model = Skill
    fields = ['skill', 'skill_level']
    template_name = 'skills/skill_form.html'
    # remember, the template_name is searched for RELATIVE to the templates directory

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SkillsIndex(LoginRequiredMixin, ListView):
    template_name = 'skills/skills_index.html'

    def get_queryset(self):
        return self.request.user.skill_set.all()