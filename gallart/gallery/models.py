from django.db import models
from django.urls import reverse
from django.conf import settings


class Genre(models.Model):
    """Model representing an artwork genre."""
    name = models.CharField(
        max_length=128, help_text='Enter an artwork genre (e.g. Science Fiction)'
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    class Meta:
        verbose_name_plural = 'Genres'


# Create your models here.
class Artwork(models.Model):
    """Model representing an artwork."""
    # Fields
    title = models.CharField(max_length=128, help_text="Title of the artwork")
    slug = models.CharField(
        max_length=128, unique=True, help_text="The slug of the artwork title"
    )
    url = models.CharField(max_length=255, help_text="Relative path to the image")

    # Relationships
    # Artwork can only have one author, authors can have multiple artworks.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False
    )
    # A genre can contain many artworks. Artworks can cover many genres.
    genre = models.ManyToManyField(
        Genre, help_text='Select a genre for this artwork'
    )

    # Timestamps
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this Artwork."""
        return reverse('gallery:show', args=(self.slug,))

    def __str__(self):
        """String for representing the Artwork object."""
        return self.title

    class Meta:
        verbose_name_plural = 'Artworks'
        ordering = ['-published_at']
