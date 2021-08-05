from django.views.generic.base import RedirectView
from django.urls import reverse


class HomeRedirectView(RedirectView):
    url = 'gallery/'
    permanent = True
