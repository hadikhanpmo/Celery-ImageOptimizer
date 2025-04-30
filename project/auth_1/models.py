from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"Image {self.id}"
