from django.db import models
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=512)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    image = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('-created', '-modified')

    def __str__(self):
        return self.name
