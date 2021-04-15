from django.urls import path,include
from .views import PostListView,PostCreateView

urlpatterns = [
    path('api/posts/',PostListView.as_view()),
    path('api/create/posts/',PostCreateView.as_view()),

]