from rest_framework import serializers
from .models import Calendar, Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['categoryId', 'categoryTitle', 'categoryColor']

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['postId', 'title', 'content', 'isFinished', 'category']

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ['calendarId', 'calendarDate', 'themeId']