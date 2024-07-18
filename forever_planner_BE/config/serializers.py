
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['categoryId', 'categoryColor', 'categoryTitle']
        read_only_fields = ['categoryId']
