from django.template.defaulttags import register

from blog.models import Comment



@register.filter()
def ranges(count= 11 ):
    return range(1, count)