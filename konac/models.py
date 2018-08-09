from django.db import models

# Create your models here.
class Comments(models.Model):
    user = models.CharField(max_length = 64)
    comment = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.size} {self.type} {self.dish} Pizza - ${self.price}"