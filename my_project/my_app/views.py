from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import MyModel, UserProfile, User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserProfileForm
from django.contrib import messages

def my_model_list(request):
    models = MyModel.objects.all()
    return render(request, 'my_model_list.html', {'models': models})

def user_profile_list(request):
    users = User.objects.all()
    print(f'User profiles queryset (in user_profile_list): {users}')
    return render(request, 'user_profile_list.html', {'users': users})

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

class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'user_profile_form.html'
    success_url = '/user_profiles/'

class UserProfileUpdateView(UpdateView):
    model = User  # Use the User model instead of UserProfile
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
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('my_model_list')
        else:
            for field, errors in form.errors.as_data().items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserProfileForm()
    return render(request, 'register.html', {'form': form})
