from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # path("", views.article_list, name="article_list"),
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
    # path("<int:pk>/", views.article_detail, name="article_detail"),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view(), name="article_detail"),
    path("<int:article_pk>/comments/", views.CommentListAPIView.as_view(), name="comment_list"),
    path("comments/<int:comments_pk>/", views.CommentDetailAPIView.as_view(), name="comment_detail"),
    path("check-sql/", views.check_sql, name="check_sql"),
    # path("html/", views.article_list_html, name="article_list_html"),
    # path("json-01/", views.json_01, name="json_01"),
    # path("json-02/", views.json_02, name="json_02"),
    # path("json-drf/", views.json_drf, name="json_drf"),
]
