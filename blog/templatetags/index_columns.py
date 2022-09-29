from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/left_column_tpl.html')
def get_left_column():
    if Post.objects.filter(category__slug='videos'):
        left_column_posts = Post.objects.filter(category__slug='videos')[0:10]
        return {"left_column_posts":left_column_posts}

@register.inclusion_tag('blog/right_column_tpl.html')
def get_right_column():
    if Post.objects.filter(category__slug='exclusives-details'):
        right_column_posts = Post.objects.filter(category__slug='exclusives-details')[0:10]
        return {"right_column_posts":right_column_posts}