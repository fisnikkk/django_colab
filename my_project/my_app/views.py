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
    search_term = request.GET.get('search', '')

    if search_term:
        object_list = MyModel.objects.filter(name__icontains=search_term)
    else:
        object_list = MyModel.objects.all()

    paginator = Paginator(object_list, 10) # Show 10 items per page

    page = request.GET.get('page')
    my_models = paginator.get_page(page)

    context = {
        'object_list': my_models,
        'search_term': search_term,
        'page_obj': my_models,
        'paginator': paginator,
    }

    return render(request, 'my_model_list.html', context)

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
    template_name = 'my_app/user_profile_list.html'
    context_object_name = 'user_profiles'

class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'my_app/user_profile_form.html'
    success_url = '/user_profiles/'

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'my_app/user_profile_form.html'
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
            login(request, user)
            return redirect('my_model_list')  # Change this to the view you want to redirect after registration
    else:
        form = UserProfileForm()
    return render(request, 'register.html', {'form': form})
