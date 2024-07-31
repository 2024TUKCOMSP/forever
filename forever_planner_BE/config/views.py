from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
import uuid
from datetime import datetime, timedelta
from .models import Calendar, Post, Category, HomeScreenSetting, ScreenSetting, Theme
from .serializers import CalendarSerializer, PostSerializer, CategorySerializer, ThemeSerializer

@api_view(['POST'])
def create_category(request):
    categoryColor = request.data.get('categoryColor')
    categoryTitle = request.data.get('categoryTitle')

    try:
        theme = Theme.objects.get(is_use=True)
    except Theme.DoesNotExist:
        return Response({'error': '테마를 찾을 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        categoryColor = int(categoryColor)
        if categoryColor < 0 or categoryColor >= len(theme.colorList):
            raise ValueError
    except (ValueError, TypeError):
        return Response({'error': '해당 카테고리의 인덱스가 존재하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['PUT'])
def edit_category(request):
    categoryId = request.data.get('categoryId')
    categoryColor = request.data.get('categoryColor')
    categoryTitle = request.data.get('categoryTitle')

    try:
        category = Category.objects.get(categoryId=categoryId)
    except Category.DoesNotExist:
        return Response({'success': False, 'error': '카테고리를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        theme = Theme.objects.get(is_use=True)
    except Theme.DoesNotExist:
        return Response({'error': '테마를 찾을 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        categoryColor = int(categoryColor)
        if categoryColor < 0 or categoryColor >= len(theme.colorList):
            raise ValueError
    except (ValueError, TypeError):
        return Response({'error': '카테고리 색상 인덱스가 유효하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    category.categoryColor = categoryColor
    category.categoryTitle = categoryTitle
    category.save()

    response_data = {'success': True}
    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_category(request, categoryId):
    try:
        category = Category.objects.get(categoryId=categoryId)

        category.is_deleted = True
        category.save()
        return Response({'success': True}, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        return Response({'success': False, 'error': '카테고리를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def calendar_all(request):
    month = request.data.get('calendarMonth')
    year = request.data.get('calendarYear')

    if not all([month, year]):
        return Response({'error': '필수 필드가 누락되었습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        month = int(month)
        year = int(year)
    except ValueError:
        return Response({'error': '월 또는 년도가 유효하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    first_day = datetime(year, month, 1)
    last_day = (first_day + timedelta(days=32)).replace(day=1) - timedelta(days=1)

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

@api_view(['GET'])
def calendar_detail(request, calendarId):
    try:
        calendar = Calendar.objects.get(calendarId=calendarId)
    except Calendar.DoesNotExist:
        return Response({'error': '일정을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

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

@api_view(['PUT'])
def post_update(request):
    post_id = request.data.get('postId')
    title = request.data.get('title')
    content = request.data.get('content', '')  
    category_id = request.data.get('categoryId')
    calendar_month = request.data.get('calendarMonth')
    calendar_year = request.data.get('calendarYear')
    calendar_date = request.data.get('calendarDate')

    if not all([post_id, title, category_id, calendar_month, calendar_year, calendar_date]):
        return Response({'error': '필수 필드가 누락되었습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        post = Post.objects.get(postId=post_id)
    except Post.DoesNotExist:
        return Response({'error': '포스트를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        category = Category.objects.get(categoryId=category_id)
    except Category.DoesNotExist:
        return Response({'error': '카테고리를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        calendar_month = int(calendar_month)
        calendar_year = int(calendar_year)
        calendar_date = int(calendar_date)
        date = datetime(year=calendar_year, month=calendar_month, day=calendar_date).date()
    except (ValueError, TypeError):
        return Response({'error': '날짜 형식이 유효하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    calendar, created = Calendar.objects.get_or_create(
        calendarDate=date,
        defaults={'themeId': uuid.uuid4()}
    )

    if not created:
        calendar.themeId = post.calendar.themeId
        calendar.save()

    post.title = title
    post.content = content
    post.category = category
    post.calendar = calendar
    post.save()

    return Response({'success': True}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def post_finish(request):
    post_id = request.data.get('postId')
    is_finished = request.data.get('isFinished')

    print(f"Received data: postId={post_id}, isFinished={is_finished}")

    if post_id is None or is_finished is None:
        return Response({'error': '필수 필드가 누락되었습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        post = Post.objects.get(postId=post_id)
    except Post.DoesNotExist:
        return Response({'error': '포스트를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

    post.isFinished = is_finished
    post.save()

    return Response({'success': True}, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_create(request):
    title = request.data.get('title')
    content = request.data.get('content', '')
    category_id = request.data.get('categoryId')
    calendar_month = request.data.get('calendarMonth')
    calendar_year = request.data.get('calendarYear')
    calendar_date = request.data.get('calendarDate')

    if not all([title, category_id, calendar_month, calendar_year, calendar_date]):
        return Response({'error': '필수 필드가 누락되었습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        calendar_month = int(calendar_month)
        calendar_year = int(calendar_year)
        calendar_date = int(calendar_date)
    except ValueError:
        return Response({'error': '월, 연도 또는 날짜가 유효하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        date = datetime(year=calendar_year, month=calendar_month, day=calendar_date)
    except ValueError:
        return Response({'error': '유효하지 않은 날짜입니다.'}, status=status.HTTP_400_BAD_REQUEST)

    calendar, created = Calendar.objects.get_or_create(
        calendarDate=date,
        defaults={'themeId': uuid.uuid4()}
    )

    try:
        category = Category.objects.get(categoryId=category_id)
    except Category.DoesNotExist:
        return Response({'error': '카테고리를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

    post = Post.objects.create(
        title=title,
        content=content,
        category=category,
        calendar=calendar
    )

    return Response({
        'success': True,
        'postId': post.postId,
        'calendarId': calendar.calendarId
    }, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def category_all(request):
    categories = Category.objects.filter(is_deleted=False)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def today_schedule(request):
    home_screen_setting = HomeScreenSetting.objects.first()
    
    if not home_screen_setting or not home_screen_setting.is_visible_today_task:
        return Response(status=status.HTTP_204_NO_CONTENT)

    today = datetime.today().date()
    
    try:
        calendar = Calendar.objects.get(calendarDate=today)
    except Calendar.DoesNotExist:
        return Response({'error': '오늘의 일정이 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

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

@api_view(['GET'])
def all_tasks(request):
    home_screen_setting = HomeScreenSetting.objects.first()

    if not home_screen_setting or not home_screen_setting.is_visible_some_task:
        return Response(status=status.HTTP_204_NO_CONTENT)

    today = datetime.today().date()
    posts = Post.objects.filter(isFinished=False)
    response_data = []

    for post in posts:
        if post.calendar is not None:
            calendar_date = post.calendar.calendarDate
            daycount = (today - calendar_date).days

            if daycount > 0:
                calendar_id = post.calendar.calendarId
                calendar_day = calendar_date.day
                post_data = {
                    'calendarId': calendar_id,
                    'calendarDate': calendar_date,
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
            continue

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_task(request):
    home_screen_setting = HomeScreenSetting.objects.first()
    
    if not home_screen_setting or not home_screen_setting.is_visible_not_yet_task:
        return Response(status=status.HTTP_204_NO_CONTENT)

    title = request.data.get('title')
    content = request.data.get('content')
    category_id = request.data.get('categoryId')
    if not all([title, content, category_id]):
        return Response({'error': '필수 필드가 누락되었습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        category = Category.objects.get(categoryId=category_id)
    except Category.DoesNotExist:
        return Response({'error': '카테고리를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

    post = Post.objects.create(
        title=title,
        content=content,
        category=category,
        isFinished=False
    )

    return Response({'success': True, 'postId': post.postId}, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def home_task(request):
    is_visible_not_yet_task = request.data.get('isVisibleNotYetTask')
    is_visible_today_task = request.data.get('isVisibleTodayTask')
    is_visible_some_task = request.data.get('isVisibleSomeTask')
    
    if any(setting is None for setting in [is_visible_not_yet_task, is_visible_today_task, is_visible_some_task]):
        return Response({'error': '모든 가시성 설정이 필요합니다.'}, status=status.HTTP_400_BAD_REQUEST)

    setting, created = HomeScreenSetting.objects.update_or_create(
        defaults={
            'is_visible_not_yet_task': is_visible_not_yet_task,
            'is_visible_today_task': is_visible_today_task,
            'is_visible_some_task': is_visible_some_task
        }
    )
    
    return Response({
        'success': True
    }, status=status.HTTP_200_OK)

@api_view(['PUT'])
def screen_theme(request):
    ScreenTheme = request.data.get('ScreenTheme')
    if not ScreenTheme:
        return Response({'error': '화면 테마가 필요합니다.'}, status=status.HTTP_400_BAD_REQUEST)
    if ScreenTheme not in ['light', 'dark']:
        return Response({'error': '유효하지 않은 화면 테마 값입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    setting, created = ScreenSetting.objects.update_or_create(id=1, defaults={'ScreenTheme': ScreenTheme})
    
    return Response({'success': True}, status=status.HTTP_200_OK)

@api_view(['GET'])
def theme_list(request):
    themes = Theme.objects.all()
    serializer = ThemeSerializer(themes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def theme_detail(request, themeId):
    try:
        theme = Theme.objects.get(themeId=themeId)
    except Theme.DoesNotExist:
        return Response({'error': '테마를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ThemeSerializer(theme)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def theme_use(request):
    theme_id = request.data.get('themeId')
    if not theme_id:
        return Response({'error': '테마 ID가 필요합니다.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        theme = Theme.objects.get(themeId=theme_id)
    except Theme.DoesNotExist:
        return Response({'error': '테마를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

    Theme.objects.update(is_use=False)
    theme.is_use = True
    theme.save()

    update_category_colors(theme)

    return Response({'message': '성공', 'is_use': theme.is_use}, status=status.HTTP_200_OK)

def update_category_colors(new_theme):
    categories = Category.objects.all()
    for category in categories:
        new_color_list = new_theme.colorList
        if category.categoryColor < len(new_color_list):
            new_color_code = new_color_list[category.categoryColor]['colorCode']
            category.categoryColor = category.categoryColor  
            category.save()
