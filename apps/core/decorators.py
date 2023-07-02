from django.shortcuts import redirect


def group_required(group_name):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            return redirect('homepage')

        return wrapper

    return decorator


def anonymous_required():
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            view = view_func(request, *args, **kwargs)
            if request.user.is_authenticated:
                return redirect('homepage')
            return view
        return wrapper

    return decorator
