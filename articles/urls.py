from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'articles', views.ArticlesView, basename='articles')
router.register(r'category', views.CategoryView, basename='category')
router.register(r'tag', views.TagView, basename='tag')

urlpatterns = [
    path('', include(router.urls))
]