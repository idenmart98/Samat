from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='images')
    head = models.TextField(max_length=30)
    descrtipton = models.TextField(max_length=1500)
    created = models.DateTimeField()


    def __str__(self):
        return self.head