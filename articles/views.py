from urllib import response
from django.shortcuts import render
from .models import Article, Category, Tag
from .serializers import ArticleSerializer, CategorySerializer, TagSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from rest_framework.decorators import action
from .permissions import IsManager
from rest_framework import status

# Create your views here.

class ArticlesView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'category__name', 'tag__name']

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Poster').exists():
            return Article.objects.filter(author=user)
        elif user.groups.filter(name='Management').exists():
            return Article.objects.all()
        else:
            return Article.objects.filter(status='published')
        
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsManager])
    def approave(self, request, pk=None):
        try:
            article = self.get_object()
            article.status = 'published'
            return response({'message' : 'Article approave and published'})
        except:
            return response({'error': 'Article not found.'}, status=status.HTTP_404_NOT_FOUND)

    
class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Poster').exists():
            return Article.objects.filter(author=user)
        elif user.groups.filter(name='Management').exists():
            return Article.objects.all()
        else:
            return Article.objects.filter(status='published')
        

class TagView(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Poster').exists():
            return Article.objects.filter(author=user)
        elif user.groups.filter(name='Management').exists():
            return Article.objects.all()
        else:
            return Article.objects.filter(status='published')
        