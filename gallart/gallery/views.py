from django.shortcuts import render
from django.views import generic

from .models import Artwork


def index(request):
    artworks = Artwork.objects.all()

    if 'user_id' in request.GET:
        artworks = artworks.filter(author=request.GET['user_id'])

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    ctx = {
        'artworks': artworks,
        'num_visits': num_visits,
    }

    return render(request, 'gallery/artworks/index.html', context=ctx)


class ArtworkDetailView(generic.DetailView):
    model = Artwork
    template_name = 'gallery/artworks/show.html'
