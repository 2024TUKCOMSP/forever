from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
import uuid

@api_view(['PUT'])
def edit_category(request):
    categoryId = request.data.get('categoryId')
    categoryColor = request.data.get('categoryColor')
    categoryTitle = request.data.get('categoryTitle')

    try:
        category = Category.objects.get(categoryId=categoryId)
        category.categoryColor = categoryColor
        category.categoryTitle = categoryTitle
        category.save()
        response_data = {'success': True}
        return Response(response_data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        return Response({'success': False, 'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_category(request):
    categoryColor = request.data.get('categoryColor')
    categoryTitle = request.data.get('categoryTitle')

    category = Category(
        categoryColor=categoryColor,
        categoryTitle=categoryTitle
    )
    category.save()

    response_data = {
        'categoryId': category.categoryId,
        'success': True
    }
    return Response(response_data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def delete_category(request, categoryId):
    try:
        category = Category.objects.get(categoryId=categoryId)
        category.delete()
        response_data = {'success': True}
        return Response(response_data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        return Response({'success': False, 'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)