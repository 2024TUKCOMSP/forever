from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer

@api_view(['PUT'])
def create_category(request):
    # 클라이언트가 보낸 데이터에서 categoryId, categoryColor, categoryTitle을 가져옵니다.
    categoryId = request.data.get('categoryId')
    categoryColor = request.data.get('categoryColor')
    categoryTitle = request.data.get('categoryTitle')

    # 카테고리 생성
    serializer = CategorySerializer(data={
        'categoryId': categoryId,
        'categoryColor': categoryColor,
        'categoryTitle': categoryTitle
    })

    if serializer.is_valid():
        serializer.save()  # 데이터베이스에 저장
        response_data = {
            'success': True
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
