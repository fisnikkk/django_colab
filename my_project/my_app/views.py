from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from .models import BlogPost, UserProfile, User



def user_profile_list(request):
    users = User.objects.all()
    print(f'User profiles queryset (in user_profile_list): {users}')
    return render(request, 'user_profile_list.html', {'users': users})

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_post'] = context.pop('blogpost')  # Rename the key
        print(f"Blog post pk: {context['blog_post'].pk}")
        return context




class BlogPostCreateView(CreateView):

    model = BlogPost
    fields = ['title', 'author', 'content']

    template_name = 'blog_post_create.html'
    success_url = reverse_lazy('blog_post_list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'author', 'content']

    template_name = 'blog_post_update.html'
    success_url = reverse_lazy('blog_post_list')

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog_post_delete.html'
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

@method_decorator(login_required, name='dispatch')
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog_post_list.html'
    context_object_name = 'blog_posts'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_post_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    print(f"Blog post pk: {context['blogpost'].pk}")
    return context