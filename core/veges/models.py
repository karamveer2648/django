from django.db import models

# Create your models here.
class recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    prep_time = models.CharField(max_length=100)
    prep_guide = models.TextField()
    image = models.ImageField(upload_to='recipe_images/')
    category = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name    
