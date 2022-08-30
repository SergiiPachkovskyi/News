from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import News, Category
from .paginations import NewsPagination
from .permission import IsAdminOrOwnerOrReadOnly, IsAdminOrReadOnly
from .serializers import NewsSerializer, CategorySerializer


class NewsListCreate(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = NewsPagination


class NewsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrOwnerOrReadOnly,)


class NewsByCategoryRetrieve(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        cat_id = self.kwargs.get('cat_id')
        return News.objects.filter(category_id=cat_id)


class NewsByUserRetrieve(generics.ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrOwnerOrReadOnly,)

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return News.objects.filter(user_id=user_id)


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
