from django.contrib import admin
from .models import Image, allImage


class ImageInLine(admin.TabularInline):
    model = Image


class BatchAdmin(admin.ModelAdmin):
    inlines = [ImageInLine]

    class Meta:
        model = allImage


admin.site.register(allImage, BatchAdmin)
