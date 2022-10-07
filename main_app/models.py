from django.db import models

# Create your models here.

class Finch(models.Model): 

    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=4)
    img = models.CharField(max_length=5000)
    bio = models.TextField(max_length=500)
    verified_finch = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']