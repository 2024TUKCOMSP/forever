# models.py

import uuid
from django.db import models

class Category(models.Model):
    categoryId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoryColor = models.IntegerField()
    categoryTitle = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryTitle
