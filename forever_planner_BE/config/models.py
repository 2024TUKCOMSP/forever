import uuid
from django.db import models

class ScreenSetting(models.Model):
    SCREEN_THEME_CHOICES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]
    ScreenTheme = models.CharField(max_length=20, choices=SCREEN_THEME_CHOICES, default='light')

class Theme(models.Model):
    themeId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    themeTitle = models.CharField(max_length=255)
    colorList = models.JSONField()
    is_use = models.BooleanField(default=False)

    def __str__(self):
        return self.themeTitle

class HomeScreenSetting(models.Model):
    settingId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_visible_not_yet_task = models.BooleanField(default=True)
    is_visible_today_task = models.BooleanField(default=True)
    is_visible_some_task = models.BooleanField(default=True)

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

