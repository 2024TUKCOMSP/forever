import uuid
from django.db import models

class Category(models.Model):
    categoryId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoryColor = models.IntegerField()
    categoryTitle = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryTitle

class Calendar(models.Model):
    calendarId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    calendarDate = models.DateField(unique=True)
    themeId = models.UUIDField(default=uuid.uuid4)

class Post(models.Model):
    postId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    isFinished = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)

