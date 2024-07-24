from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import uuid
from datetime import datetime, timedelta
from .models import Calendar, Post, Category, HomeScreenSetting, ScreenSetting
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
    month = request.data.get('calendarMonth')
    year = request.data.get('calendarYear')

    if not all([month, year]):
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        month = int(month)
        year = int(year)
    except ValueError:
        return Response({'error': 'Invalid month or year'}, status=status.HTTP_400_BAD_REQUEST)

    # 해당 월의 첫 번째 날과 마지막 날 계산
    first_day = datetime(year, month, 1)
    last_day = (first_day + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    # 해당 월의 모든 날짜에 대해 Calendar 객체 조회
    calendars = Calendar.objects.filter(calendarDate__year=year, calendarDate__month=month)

    response_data = []
    for calendar in calendars:
        posts = Post.objects.filter(calendar=calendar)
        post_serializer = PostSerializer(posts, many=True)
        calendar_data = {
            "calendarId": calendar.calendarId,
            "calendarDate": calendar.calendarDate.day,
            "themeId": calendar.themeId,
            "post": post_serializer.data
        }
        response_data.append(calendar_data)

    return Response(response_data)

# 특정 일정 조회 함수
@api_view(['GET'])
def calendar_detail(request, calendarId):
    try:
        calendar = Calendar.objects.get(calendarId=calendarId)
    except Calendar.DoesNotExist:
        return Response({'error': 'Calendar not found'}, status=status.HTTP_404_NOT_FOUND)

    posts = Post.objects.filter(calendar=calendar)
    response_data = []

    for post in posts:
        category_serializer = CategorySerializer(post.category)
        post_data = {
            "postId": post.postId,
            "title": post.title,
            "content": post.content,
            "isFinished": post.isFinished,
            "categoryColor": post.category.categoryColor,
            "categoryTitle": category_serializer.data['categoryTitle']
        }
        response_data.append(post_data)

    return Response(response_data)

# 일정 수정 함수
@api_view(['PUT'])
def post_update(request):
    post_id = request.data.get('postId')
    title = request.data.get('title')
    content = request.data.get('content')
    category_id = request.data.get('categoryId')

    if not all([post_id, title, content, category_id]):
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Post 객체 조회
        post = Post.objects.get(postId=post_id)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        # Category 객체 조회
        category = Category.objects.get(categoryId=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    # Post 객체 업데이트
    post.title = title
    post.content = content
    post.category = category
    post.save()

    return Response({'success': True}, status=status.HTTP_200_OK)

# 일정 완료 상태 수정 함수
@api_view(['PUT'])
def post_finish(request):
    # 요청 데이터에서 postId와 isFinished를 추출
    post_id = request.data.get('postId')
    is_finished = request.data.get('isFinished')

    # 디버깅 출력을 추가
    print(f"Received data: postId={post_id}, isFinished={is_finished}")

    # 필수 데이터가 모두 있는지 확인
    if post_id is None or is_finished is None:
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Post 객체 조회
        post = Post.objects.get(postId=post_id)
    except Post.DoesNotExist:
        # 게시물이 존재하지 않는 경우
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    # 완료 상태 업데이트
    post.isFinished = is_finished
    post.save()

    # 성공 응답 반환
    return Response({'success': True}, status=status.HTTP_200_OK)

# 일정 추가 함수
@api_view(['POST'])
def post_create(request):
    # 요청 데이터에서 값 추출
    title = request.data.get('title')
    content = request.data.get('content')
    category_id = request.data.get('categoryId')
    calendar_month = request.data.get('calendarMonth')
    calendar_year = request.data.get('calendarYear')
    calendar_date = request.data.get('calendarDate')

    # 필수 데이터 확인
    if not all([title, content, category_id, calendar_month, calendar_year, calendar_date]):
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    # 데이터 타입 변환 및 검증
    try:
        calendar_month = int(calendar_month)
        calendar_year = int(calendar_year)
        calendar_date = int(calendar_date)
    except ValueError:
        return Response({'error': 'Invalid month, year, or date'}, status=status.HTTP_400_BAD_REQUEST)

    # 날짜를 datetime 객체로 변환
    try:
        date = datetime(year=calendar_year, month=calendar_month, day=calendar_date)
    except ValueError:
        return Response({'error': 'Invalid date'}, status=status.HTTP_400_BAD_REQUEST)

    # 날짜에 해당하는 Calendar 객체 조회 또는 생성
    calendar, created = Calendar.objects.get_or_create(
        calendarDate=date,
        defaults={'themeId': uuid.uuid4()}
    )

    # 카테고리 조회
    try:
        category = Category.objects.get(categoryId=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    # Post 객체 생성 및 저장
    post = Post.objects.create(
        title=title,
        content=content,
        category=category,
        calendar=calendar
    )

    # 성공 응답 반환
    return Response({
        'success': True,
        'postId': post.postId,
        'calendarId': calendar.calendarId
    }, status=status.HTTP_201_CREATED)

    # 성공 응답 반환
    return Response({
        'success': True,
        'postId': post.postId,
        'calendarId': calendar.calendarId
    }, status=status.HTTP_201_CREATED)

# 일정 재추가 함수
@api_view(['POST'])
def post_recreate(request):
    calendar_id = request.data.get('calendarId')
    title = request.data.get('title')
    content = request.data.get('content')
    category_id = request.data.get('categoryId')

    if not all([calendar_id, title, content, category_id]):
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        calendar = Calendar.objects.get(calendarId=calendar_id)
    except Calendar.DoesNotExist:
        return Response({'error': 'Calendar not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        category = Category.objects.get(categoryId=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    post = Post.objects.create(
        title=title,
        content=content,
        category=category,
        calendar=calendar
    )

    return Response({'success': True, 'postId': post.postId}, status=status.HTTP_201_CREATED)


# 모든 카테고리 조회 함수
@api_view(['GET'])
def category_all(request):
    # 모든 카테고리를 검색하고 직렬화하여 반환
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
    
# 오늘의 일정 출력 함수
@api_view(['GET'])
def today_schedule(request):
    # 홈 화면 설정을 가져옵니다.
    home_screen_setting = HomeScreenSetting.objects.first()
    
    # 설정에 따라 오늘의 일정을 출력하지 않도록 합니다.
    if not home_screen_setting or not home_screen_setting.is_visible_today_task:
        return Response(status=status.HTTP_204_NO_CONTENT)

    today = datetime.today().date()
    
    # 오늘의 일정을 가져옵니다.
    try:
        calendar = Calendar.objects.get(calendarDate=today)
    except Calendar.DoesNotExist:
        return Response({'error': 'No schedule for today'}, status=status.HTTP_404_NOT_FOUND)

    posts = Post.objects.filter(calendar=calendar)
    response_data = {
        'calendarDate': calendar.calendarDate.day,
        'post': []
    }
    
    for post in posts:
        category_serializer = CategorySerializer(post.category)
        post_data = {
            'postId': post.postId,
            'title': post.title,
            'content': post.content,
            'isFinished': post.isFinished,
            'categoryColor': post.category.categoryColor,
            'categoryTitle': category_serializer.data['categoryTitle']
        }
        response_data['post'].append(post_data)

    return Response(response_data, status=status.HTTP_200_OK)

#남은 할일
@api_view(['GET'])
def all_tasks(request):
    # 홈 화면 설정을 가져옵니다.
    home_screen_setting = HomeScreenSetting.objects.first()
    
    # 설정에 따라 할 일 목록을 출력하지 않도록 합니다.
    if not home_screen_setting or not home_screen_setting.is_visible_some_task:
        return Response(status=status.HTTP_204_NO_CONTENT)

    today = datetime.today().date()

    # isFinished가 False인 포스트를 필터링합니다.
    posts = Post.objects.filter(isFinished=False)
    response_data = []

    for post in posts:
        if post.calendar is not None:
            calendar_date = post.calendar.calendarDate
            daycount = (today - calendar_date).days

            # D-day가 지난 경우에만 출력합니다.
            if daycount > 0:
                calendar_id = post.calendar.calendarId
                calendar_day = calendar_date.day
                post_data = {
                    'calendarId': calendar_id,
                    'calendarDate': calendar_day,
                    'daycount': f'+{daycount}일',
                    'post': {
                        'postId': post.postId,
                        'title': post.title,
                        'content': post.content,
                        'isFinished': post.isFinished
                    }
                }
                response_data.append(post_data)
        else:
            # 캘린더가 없는 포스트는 D-day 계산이 불가능하므로 생략합니다.
            continue

    return Response(response_data, status=status.HTTP_200_OK)

#언젠가 할일
@api_view(['POST'])
def add_task(request):
    # 홈 화면 설정을 가져옵니다.
    home_screen_setting = HomeScreenSetting.objects.first()
    
    # 설정에 따라 할 일 추가를 허용하지 않도록 합니다.
    if not home_screen_setting or not home_screen_setting.is_visible_not_yet_task:
        return Response(status=status.HTTP_204_NO_CONTENT)

    title = request.data.get('title')
    content = request.data.get('content')
    category_id = request.data.get('categoryId')

    # 필요한 필드가 누락된 경우 에러를 반환합니다.
    if not all([title, content, category_id]):
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    # 카테고리를 찾습니다.
    try:
        category = Category.objects.get(categoryId=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    # 캘린더 없이 언젠가 할 일을 추가합니다.
    post = Post.objects.create(
        title=title,
        content=content,
        category=category,
        isFinished=False
    )

    # 성공적으로 추가된 할 일의 postId를 반환합니다.
    return Response({'success': True, 'postId': post.postId}, status=status.HTTP_201_CREATED)


# 홈 화면 설정
@api_view(['PUT'])
def home_task(request):
    # 클라이언트로부터 가시성 설정 값을 가져옵니다.
    is_visible_not_yet_task = request.data.get('isVisibleNotYetTask')
    is_visible_today_task = request.data.get('isVisibleTodayTask')
    is_visible_some_task = request.data.get('isVisibleSomeTask')
    
    # 모든 설정 값이 제공되지 않으면 에러를 반환합니다.
    if any(setting is None for setting in [is_visible_not_yet_task, is_visible_today_task, is_visible_some_task]):
        return Response({'error': 'All visibility settings are required'}, status=status.HTTP_400_BAD_REQUEST)

    # HomeScreenSetting 모델에 가시성 설정 값을 업데이트하거나 생성합니다.
    setting, created = HomeScreenSetting.objects.update_or_create(
        defaults={
            'is_visible_not_yet_task': is_visible_not_yet_task,
            'is_visible_today_task': is_visible_today_task,
            'is_visible_some_task': is_visible_some_task
        }
    )
    
    # 성공적으로 업데이트된 가시성 설정 값을 반환합니다.
    return Response({
        'success': True
    }, status=status.HTTP_200_OK)

# 화면 모드 설정
@api_view(['PUT'])
def screen_theme(request):
    # 클라이언트로부터 ScreenTheme 값
    ScreenTheme = request.data.get('ScreenTheme')
    if not ScreenTheme:
        return Response({'error': 'ScreenTheme is required'}, status=status.HTTP_400_BAD_REQUEST)
    if ScreenTheme not in ['light', 'dark']:
        return Response({'error': 'Invalid ScreenTheme value'}, status=status.HTTP_400_BAD_REQUEST)
    
    # ScreenSetting 모델에 ScreenTheme 값을 업데이트하거나 생성합니다.
    setting, created = ScreenSetting.objects.update_or_create(id=1, defaults={'ScreenTheme': ScreenTheme})
    
    return Response({'success': True}, status=status.HTTP_200_OK)