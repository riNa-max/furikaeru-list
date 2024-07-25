from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import TodoList,TodoStatus
from .forms import TodoForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LogoutView



@method_decorator(login_required,name='dispatch')
class List(ListView):
    template_name='list.html'
    model=TodoList
    context_object_name='todo_list'
    ordering=['duedate']

    def get_queryset(self):
        return TodoList.objects.filter(user=self.request.user).order_by('duedate')

@method_decorator(login_required,name='dispatch')
class Detail(DetailView):
    template_name='detail.html'
    model=TodoList

@method_decorator(login_required,name='dispatch')
class Create(CreateView):
    template_name='create.html'
    model=TodoList
    form_class=TodoForm
    success_url=reverse_lazy('list')

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

@method_decorator(login_required,name='dispatch')
class Delete(DeleteView):
    template_name='delete.html'
    model=TodoList
    success_url=reverse_lazy('list')

@method_decorator(login_required,name='dispatch')
class Update(UpdateView):
    template_name='update.html'
    model=TodoList
    form_class=TodoForm
    success_url=reverse_lazy('list')

@method_decorator(login_required,name='dispatch')
class EndList(ListView):
    template_name='end_list.html'
    model=TodoList
    context_object_name='todo_list'

    def get_queryset(self):
        return TodoList.objects.filter(user=self.request.user).order_by('duedate')


def signupfunc(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.create_user(username,'',password)
            user.save()
            return render(request,'login.html',{})
        except IntegrityError:
            return render(request,'signup.html',{'error':'このユーザーはすでに登録されています'})
    return render(request,'signup.html',{})

def loginfunc(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('list')
        else:
            return render(request,'login.html',{'context':'not logged in'})
    return render(request,'login.html',{'context':'get method'})

class Logout(LogoutView):
    template_name='logout.html'
