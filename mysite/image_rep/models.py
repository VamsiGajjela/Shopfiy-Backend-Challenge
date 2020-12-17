from django.db import models
from datetime import date
import django.utils

class Image(models.Model):
    day = date.today()
    date_published = models.DateField(blank=True, null=True, default=django.utils.timezone.now)
    image_name = models.CharField(blank=True, null=True, max_length=50)
    image_1 = models.ImageField(upload_to='images/{}/{}/{}'.format(day.year, day.month, day.day),blank=True, null=True)
    image_2 = models.ImageField(upload_to='images/{}/{}/{}'.format(day.year, day.month, day.day),blank=True, null=True)
    image_3 = models.ImageField(upload_to='images/{}/{}/{}'.format(day.year, day.month, day.day),blank=True, null=True)
    image_4 = models.ImageField(upload_to='images/{}/{}/{}'.format(day.year, day.month, day.day),blank=True, null=True)
    image_5 = models.ImageField(upload_to='images/{}/{}/{}'.format(day.year, day.month, day.day),blank=True, null=True)
    
    def __str__(self):
        return "Title: {}".format(self.image_name)

    def __repr__(self):
        return self.image_name

    
