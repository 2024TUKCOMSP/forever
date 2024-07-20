from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Calendar, Post, Category
from .serializers import CalendarSerializer, PostSerializer, CategorySerializer

# 카테고리 수정 함수
@api_view(['PUT'])
def edit_category(request):
    # 카테고리 ID, 색상 및 제목을 가져옴
    categoryId = request.data.get('categoryId')
    categoryColor = request.data.get('categoryColor')
    categoryTitle = request.data.get('categoryTitle')

    try:
        # 카테고리를 검색하고 수정
        category = Category.objects.get(categoryId=categoryId)
        category.categoryColor = categoryColor
        category.categoryTitle = categoryTitle
        category.save()
        response_data = {'success': True}
        return Response(response_data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        # 카테고리를 찾을 수 없는 경우
        return Response({'success': False, 'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

# 카테고리 생성 함수
@api_view(['POST'])
def create_category(request):
    # 요청에서 카테고리 색상 및 제목을 가져옴
    categoryColor = request.data.get('categoryColor')
    categoryTitle = request.data.get('categoryTitle')

    # 새로운 카테고리 생성
    category = Category(
        categoryColor=categoryColor,
        categoryTitle=categoryTitle
    )
    category.save()

    # 데이터 생성 및 반환
    response_data = {
        'categoryId': category.categoryId,
        'success': True
    }
    return Response(response_data, status=status.HTTP_201_CREATED)

# 카테고리 삭제 함수
@api_view(['DELETE'])
def delete_category(request, categoryId):
    try:
        # 해당 카테고리를 검색하고 삭제
        category = Category.objects.get(categoryId=categoryId)
        category.delete()
        response_data = {'success': True}
        return Response(response_data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        # 카테고리를 찾을 수 없는 경우
        return Response({'success': False, 'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
    
# 전체 일정 조회 함수
@api_view(['POST'])
def calendar_all(request):
    # 요청에서 월과 연도를 가져옴
    month = request.data.get('calendarMonth')
    year = request.data.get('calendarYear')

    # 해당 월과 연도의 일정 확인
    calendars = Calendar.objects.filter(calendarDate__year=year, calendarDate__month=month)
    serializer = CalendarSerializer(calendars, many=True)
    return Response(serializer.data)

# 특정 일정 조회 함수
@api_view(['GET'])
def calendar_detail(request, calendarId):
    try:
        # 해당 ID의 일정을 검색
        calendar = Calendar.objects.get(calendarId=calendarId)
    except Calendar.DoesNotExist:
        # 일정을 찾을 수 없는 경우
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # 해당 게시물 데이터를  반환
    serializer = PostSerializer(calendar.post)
    return Response(serializer.data)

# 일정 수정 함수
@api_view(['PUT'])
def post_update(request):
    try:
        # 해당 ID의 게시물을 검색
        post = Post.objects.get(postId=request.data.get('postId'))
    except Post.DoesNotExist:
        # 게시물을 찾을 수 없는 경우
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # 게시물 데이터를 업데이트
    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 일정 완료 상태 수정 함수
@api_view(['PUT'])
def post_finish(request):
    try:
        # 해당 ID의 게시물을 검색
        post = Post.objects.get(postId=request.data.get('postId'))
    except Post.DoesNotExist:
        # 게시물을 찾을 수 없는 경우
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # 완료 상태를 업데이트하고 저장
    post.isFinished = request.data.get('isFinished')
    post.save()
    return Response({'success': True})

# 일정 추가 함수
@api_view(['POST'])
def post_create(request):
    # 요청 데이터를 저장
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        post = serializer.save()
        return Response({'success': True, 'postId': post.postId})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 모든 카테고리 조회 함수
@api_view(['GET'])
def category_all(request):
    # 모든 카테고리를 검색하고 직렬화하여 반환
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
