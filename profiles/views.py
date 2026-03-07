from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from profiles.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ProfilesListView(LoginRequiredMixin, ListView):
    model = Profile
    fields = ['name', 'email', 'job', 'age', 'bio']
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'
    ordering = '-date_created'
    login_url = 'users:login'

class ProfilesCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['name', 'email', 'job', 'age', 'bio']
    template_name = 'profiles/profile.html'
    success_url = reverse_lazy('dashboard')  
    login_url = 'users:login'

class ProfilesUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['name', 'email', 'job', 'age', 'bio']
    template_name = 'profiles/profile.html'
    success_url = reverse_lazy('dashboard')  
    login_url = 'users:login'

class ProfilesDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'profiles/profile.html'
    success_url = reverse_lazy('dashboard')  
    login_url = 'users:login'

