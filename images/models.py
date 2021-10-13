from django.db import models
from django.db.models.lookups import StartsWith

SITE = "SITE"
GALLERY = "GALLERY"
KARUSEL = "KARUSEL"

STATUS_CHOICES = (
    (SITE, "Site"),
    (GALLERY, "GAllery"),
    (KARUSEL, "Karusel"),
)
class Images(models.Model):
    image = models.ImageField(upload_to='images')
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default=SITE)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
# Create your models here.
