from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import MyModel, UserProfile
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserProfileForm
from django.contrib import messages  # Add this import at the beginning of the file
from django.contrib.auth.models import User

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
    model = User
    template_name = 'user_profile_list.html'
    context_object_name = 'users'

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
    model = User
    template_name = 'user_profile_confirm_delete.html'
    success_url = '/user_profiles/'

def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)  # Ensure this line is being executed
            login(request, user)
            return redirect('my_model_list')
        else:
            for field, errors in form.errors.as_data().items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserProfileForm()
    return render(request, 'register.html', {'form': form})
