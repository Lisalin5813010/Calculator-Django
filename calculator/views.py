
from matplotlib import pyplot as plt
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from calculator.forms import RegisterForm, LoginForm
# Create your views here.
aString= ['calculator','people','chart','todoapp','exampleView','logout']

def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "calculator/register.html", {"form": form})
    else:
        form = RegisterForm(request.POST)
        user_type = request.POST.get('user')
        if form.is_valid()& (user_type is not None):
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("calculator")
        else:
            return render(request, "calculator/register.html", {"form": form})

def sign_in(request):
    if request.method == 'GET':
      form = LoginForm()
      return render(request, 'calculator/login.html', {'form': form})
    else:
      print(request)
      form = LoginForm(request.POST)
      if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user:
          login(request, user)
          return redirect("calculator")
      return render(request, 'calculator/login.html', {'form': form})



@login_required
def sign_out(request):
    logout(request)
    return redirect('login')

# Chart view which will be inhereted by chartView.py



class Chart(LoginRequiredMixin, TemplateView):
    template_name = 'calculator/extendedhtml/chart.html'


# Person view which will be inhereted by personView.py


class People(LoginRequiredMixin, TemplateView):

    template_name = 'calculator/extendedhtml/people.html'


# calculator view which will be inhereted by calculatorView.py


class Calculator(LoginRequiredMixin, TemplateView):

    template_name = "calculator/extendedhtml/calculator.html"

# calculator view which will be inhereted by TodoappView.py


class Todoapp(LoginRequiredMixin, TemplateView):
    template_name = 'calculator/extendedhtml/todolist.html'
