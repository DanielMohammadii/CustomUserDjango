from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.urls import reverse_lazy # new
from .models import Article
from  django.contrib.auth.mixins import  LoginRequiredMixin

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin,DetailView): # new
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin,UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin,DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin,CreateView): # new
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)
    login_url = 'login'


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

