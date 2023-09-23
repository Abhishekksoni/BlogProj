from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# def home(request):
#     context={
#         'posts':Post.objects.all()
#     }
#     return render(request, 'index.html',context)

def about(request):
    return render(request ,'blog1/about.html', {'title': "About"})


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ["-date_posted"]
    template_name = 'blog1/index.html'

class PostDetailView(LoginRequiredMixin,  DetailView):
    model = Post   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content'] 
    template_name = 'blog1/post_form.html'
      

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog1/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog1/post_delete.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
