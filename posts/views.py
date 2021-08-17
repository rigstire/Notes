from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Notes
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(ListView):
    template_name = 'home.html'
    model = Notes

class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notes_detail.html'

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title','body']
    template_name = 'post_new.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NotesUpdateView(UpdateView):
    model = Notes
    template_name = 'notes_update.html'
    fields = ['title','body']

class NotesDeleteView(DeleteView):
    model = Notes
    template_name = 'notes_delete.html'
    success_url = reverse_lazy('home')

