from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # What tag applied to what obj
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type (product, ...) -> find table 
    # id -> find record
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object  = GenericForeignKey()