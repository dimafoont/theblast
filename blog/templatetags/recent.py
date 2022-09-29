from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/recent_tpl.html')
def get_recent():
    recent = Post.objects.all()[0:10]
    return {"recent":recent}

@register.inclusion_tag('blog/trending_tpl.html')
def get_trending(cnt=5):
    trending = Post.objects.order_by('-views')[:cnt]
    return {"trending":trending}