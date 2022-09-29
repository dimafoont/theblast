from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, TemplateView
from django.http import JsonResponse
from django.db.models import F

from blog.models import Post, Category, Single

class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'The Blast - Breaking Celebrity News'
        context['total_obj'] = Post.objects.count()
        return context

    def get_queryset(self):
        count_obj = Post.objects.count()
        posts = Post.objects.filter(pk__lte=count_obj-3)[0:10]
        return posts

def load_more(request):
    count_obj = Post.objects.count()
    total_item = int(request.GET.get('total_item'))
    limit = 10
    post_obj = list(Post.objects.filter(pk__lte=count_obj-3).values()[total_item:total_item+limit])
    data = {
        'posts':post_obj
    }
    return JsonResponse(data=data)

class PostsByCategory(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 10
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        context['thiscategory'] = self.kwargs['slug']
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])


class GetPost(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object.category.slug
        photo = self.object.photo.url
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        context['title'] = Post.objects.get(slug=self.kwargs['slug'])
        context['posts'] = Post.objects.filter(category__slug=category).exclude(pk = self.object.id)[0:6]
        context['category'] = Post.objects.filter(category__slug=self.kwargs['slug'])
        return context

class GetSinglePost(DetailView):
    model = Single
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Single.objects.get(slug=self.kwargs['slug'])
        return context


# Create your views here.
