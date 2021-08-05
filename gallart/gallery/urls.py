from django.urls import path

from . import views

# App namespace for urls
app_name = 'gallery'

# Prefixed by '/gallery/'.
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.ArtworkDetailView.as_view(), name='show'),
]
