from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_list_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class IndexView(TemplateView):
    """
    class base view to show index page
    """
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'farimah'
        return context
    

"""class base view

"""

"""class RedirectToMaktab(RedirectView):

    url = 'https://maktabkhooneh.com'


    def get_redirect_url(self, *args, **kwargs):
        post = get_list_or_404(Post, id=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)"""


class PostListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = 'blog:post_view'
    # model = Post
    queryset = Post.objects.filter(status=True)
    paginate_by = 2
    ordering = '-id'

    # def get_queryset(self):
    #     posts = Post.objects.all()
    #     return posts

    context_object_name = 'posts'
 

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'post'


"""
class PostCreateView(FormView):
    template_name = "blog/contact.html"
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.save()
        return super(PostCreateView, self).form_valid(form)

"""

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    # fields = ['author', 'status', 'title', 'content', 'category', 'published_date']
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostEditView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = "/blog/post/"

