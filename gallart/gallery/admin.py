from django.contrib import admin

from .models import Artwork, Genre

# Register your models here.
admin.site.register(Artwork)
admin.site.register(Genre)
