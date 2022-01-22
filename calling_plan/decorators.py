from functools import wraps

from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(func):
    wraps(func)

    def wraper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("pages:home")
        else:
            return func(request, *args, **kwargs)

    return wraper_func


def allowed_users(allowed_roles=[]):
    def decorator(func):
        def wraper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse("Acesso Negado")

        return wraper_func

    return decorator


def admin_only(func):
    wraps(func)

    def wraper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group in "admin":
            return func(request, *args, **kwargs)
        if group == "users":
            return redirect("pages:users")
        else:
            return HttpResponse("Acesso Negado")

    return wraper_func
