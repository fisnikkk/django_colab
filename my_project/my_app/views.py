from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import MyModel
from django.db.models import Q
from django.core.paginator import Paginator

class MyModelListView(ListView):
    model = MyModel
    template_name = 'my_model_list.html'
    paginate_by = 10  # Show 10 items per page

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get("search", "")
        if search_term:
            queryset = queryset.filter(Q(name__icontains=search_term) | Q(description__icontains=search_term))
        return queryset

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
