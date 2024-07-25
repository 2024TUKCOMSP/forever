from rest_framework import serializers
from .models import Calendar, Post, Category,Theme

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['categoryId', 'categoryTitle', 'categoryColor']

    def validate_categoryColor(self, value):
        if not (value.startswith("#") and len(value) in [4, 7]):
            raise serializers.ValidationError("Invalid category color")
        return value

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['postId', 'title', 'content', 'isFinished', 'category']

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ['calendarId', 'calendarDate', 'themeId']

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['themeId','themeTitle','colorList']