from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import MyModel
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render

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
