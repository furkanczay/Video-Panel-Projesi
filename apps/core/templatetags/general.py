from django import template
from apps.core.models import Users, Videos
from django.template.defaultfilters import stringfilter
import re

register = template.Library()


@register.simple_tag()
def students_count():
    students = Users.objects.filter(groups__name='Öğrenci')
    return students.count()


@register.simple_tag()
def instructors_count():
    instructors = Users.objects.filter(groups__name='Eğitmen')
    return instructors.count()


@register.filter(name='usermention', is_safe=True)
@stringfilter
def usermention(value):
    value = re.sub(r'@(\w+)', r'<a class="text-blue-800" href="/\1/">@\1</a>', value)
    return value


@register.simple_tag()
def videos_count():
    videos = Videos.objects.all()
    return videos.count()
