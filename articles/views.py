from django.shortcuts import render
from .models import Article, Category, Tag
from .serializers import ArticleSerializer, CategorySerializer, TagSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsInGroupsPerm
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

# Create your views here.

class ArticlesView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsInGroupsPerm(['Management', 'Poster'])]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'category__name', 'tag__name']  # Fixed typo

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Poster').exists():
            return Article.objects.filter(author=user)
        return super().get_queryset()

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsInGroupsPerm(['Management', 'Poster'])]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class TagView(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated, IsInGroupsPerm(['Management', 'Poster'])]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']