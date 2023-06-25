from django import template
from apps.core.models import Users, Videos

register = template.Library()


@register.simple_tag()
def students_count():
    students = Users.objects.filter(groups__name='Öğrenci')
    return students.count()


@register.simple_tag()
def instructors_count():
    instructors = Users.objects.filter(groups__name='Eğitmen')
    return instructors.count()


@register.simple_tag()
def videos_count():
    videos = Videos.objects.all()
    return videos.count()
