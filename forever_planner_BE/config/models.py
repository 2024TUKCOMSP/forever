import uuid
from django.db import models

class Category(models.Model):
    categoryId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoryColor = models.IntegerField()
    categoryTitle = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryTitle

class Post(models.Model):
    postId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    isFinished = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Calendar(models.Model):
    calendarId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    calendarDate = models.DateField()
    themeId = models.UUIDField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
