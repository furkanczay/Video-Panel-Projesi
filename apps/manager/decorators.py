from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import resolve_url


def staff_login_required(view_func):
    decorated_view_func = staff_member_required(login_url='admin_login')(view_func)
    return decorated_view_func
