from django.db import models
from datetime import date
import django.utils


class allImage(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50, default='')


class Image(models.Model):
    batch = models.ForeignKey(allImage, on_delete=models.CASCADE, null=True)
    day = date.today()
    date_published = models.DateField(blank=True, null=True, default=django.utils.timezone.now)
    image_name = models.CharField(blank=True, null=True, max_length=50, default='')
    image = models.ImageField(upload_to='images/{}/{}/{}'.format(day.year, day.month, day.day),blank=True, null=True)

    def __str__(self):
        return str(self.image_name)

    def __repr__(self):
        return str(self.image_name)


