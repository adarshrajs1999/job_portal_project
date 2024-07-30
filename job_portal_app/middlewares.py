from django.shortcuts import redirect, render
from django.urls import reverse
from django.conf import settings



class Login_required_middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = [reverse(url) for url in settings.EXEMPT_URLS]

    def __call__(self, request):
        response = self.get_response(request)
        if not request.user.is_authenticated:
            if request.path not in self.exempt_urls and response.status_code != 404:
                return redirect(settings.LOGIN_URL)
        return response


class Invalid_url_middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return render(request, '404.html', status=404)
        return response


