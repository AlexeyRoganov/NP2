from django.urls import path
from .views import PostsList, PostsDetail  # импортируем наше представление

urlpatterns = [path('', PostsList.as_view()),
               path('<int:pk>', PostsDetail.as_view())]