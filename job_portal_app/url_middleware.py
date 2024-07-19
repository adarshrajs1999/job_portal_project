from django.http import Http404
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


class Url_middleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            return render(request, '404.html')
        return None