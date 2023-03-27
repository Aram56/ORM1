from django.db import models
from django.utils.text import slugify

from django.urls import reverse

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField(max_length=50)
    lte_exists = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, primary_key=True)


    def __str__(self):
        return self.name
    
    
    # def save(self):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super().save()


