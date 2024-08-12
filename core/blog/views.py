from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Post
from .forms import PostForm


class SampleView(TemplateView):
    """
    a class based view to show sample page
    """
    template_name = 'sample.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        return context


class RedirectToGoogle(RedirectView):
    url = 'https://google.com'


class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "blog.view_post"
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3
    # http://127.0.0.1:8000/blog/posts/?page=2
    ordering = '-id'

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(DetailView):
    model = Post


'''class PostCreateView(FormView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = '/blog/posts/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

'''


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/posts/'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/posts'
