from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import MyModel, UserProfile
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserProfileForm

def my_model_list(request):
    models = MyModel.objects.all()
    return render(request, 'my_model_list.html', {'models': models})


class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'my_model_detail.html'

class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'my_model_create.html'
    success_url = reverse_lazy('my_model_list')

class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'my_model_update.html'
    success_url = reverse_lazy('my_model_list')

class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'my_model_delete.html'
    success_url = '/'

class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'user_profile_list.html'  # Make sure this line matches the file name in your templates folder
    context_object_name = 'user_profiles'


class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile_form.html'
    success_url = '/user_profiles/'

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile_form.html'
    success_url = '/user_profiles/'

class UserProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = 'my_app/user_profile_confirm_delete.html'
    success_url = '/user_profiles/'

def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)  # Add this line to create a UserProfile instance
            login(request, user)
            return redirect('my_model_list')
    else:
        form = UserProfileForm()
    return render(request, 'register.html', {'form': form})

