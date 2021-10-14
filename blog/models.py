from django.db import models


SITE = "SITE"
BLOG = "BLOG"

POST_STATUS = (
    (SITE, "Site"),
    (BLOG, "BLOG")
)

class Post(models.Model):
    status=models.CharField(max_length=10, choices=POST_STATUS, default=SITE)
    image = models.ImageField(upload_to='images')
    head = models.TextField(max_length=30)
    descrtipton = models.TextField(max_length=1500)
    created = models.DateTimeField()


    def __str__(self):
        return self.head
