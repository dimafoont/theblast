from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/relevant_tpl.html')
def get_relevant():
    posts_count = Post.objects.count()
    if posts_count >= 3:
        post1 = Post.objects.get(pk=posts_count)
        post2 = Post.objects.get(pk=posts_count-1)
        post3 = Post.objects.get(pk=posts_count-2)
        return {"post1":post1, "post2":post2, "post3":post3,}
    else:
        pass