from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import New
from .forms import NewForm
from .filters import NewFilter


class NewList(ListView):
    model = New
    template_name = 'new/default.html'
    ordering = ['-date']
    ontext_object_name = 'new'
    paginate_by = 10

class SearchList(ListView):
    model = New
    ordering = ['-date']
    template_name = 'new/search.html'
    context_object_name = 'new'
    paginate_by = 10



    def get_filter(self):
        return NewFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {**super().get_context_data(*args, **kwargs), 'filter': self.get_filter(), }

class Newid(DetailView):
    model = New
    template_name = 'new/news_id.html'
    context_object_name = 'new'

class NewCreate(CreateView):
    model = New
    form_class = NewForm
    template_name = 'new/create.html'


class NewUpdate(UpdateView):
    model = New
    form_class = NewForm
    template_name = 'new/create.html'

class NewDelete(DeleteView):
    model = New
    template_name = 'new/news_delete.html'
    success_url = '/news/'




def create_New(request):
    error = ''
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = NewForm()
    data = {'form': form, 'error': error}
    return render(request, 'new/create.html',  data)
