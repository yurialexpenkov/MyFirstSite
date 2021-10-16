from django.urls import path
from app_news.views import NewsFormView, NewsEditFormView, NewsListView, NewsDetailView, MyCommentFormView, response_to_search

urlpatterns = [
    path('create/', NewsFormView.as_view()),
    path('<int:profile_id>/edit/', NewsEditFormView.as_view()),
    path('', NewsListView.as_view(), name='news'),
    path('<int:pk>/', NewsDetailView.as_view()),
    path('<int:profile_id>/add_comment/', MyCommentFormView.as_view()),
    path('response_to_search/', response_to_search, name='search'),
    path('response_to_search/<int:pk>/', NewsDetailView.as_view(), name='search'),
    path('response_to_search/<int:profile_id>/edit/', NewsEditFormView.as_view()),
]
