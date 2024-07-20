from rest_framework import serializers
from .models import Calendar, Post, Category

class PostSerializer(serializers.ModelSerializer):
    category = serializers.UUIDField()
    isFinished = serializers.BooleanField(required=False, default=False)  # Optional field with a default value

    class Meta:
        model = Post
        fields = ['postId', 'title', 'content', 'isFinished', 'category']

    def create(self, validated_data):
        category_id = validated_data.pop('category')
        category = Category.objects.get(categoryId=category_id)
        post = Post.objects.create(category=category, **validated_data)
        return post

class CalendarSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Calendar
        fields = ['calendarId', 'calendarDate', 'themeId', 'post']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['categoryId', 'categoryTitle', 'categoryColor']
