from django import template
from blog.models import Category, Single

register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_menu():
    categories = Category.objects.all()
    return {"categories": categories}


@register.inclusion_tag('blog/menu_tpl_single.html')
def show_menu_single():
    singlePages = Single.objects.all()
    return {"singlePages": singlePages}

@register.inclusion_tag('blog/menu_tpl_footer.html')
def show_menu_footer():
    categories = Category.objects.all()
    return {"categories": categories}
