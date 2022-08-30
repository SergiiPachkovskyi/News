from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import News
from .permission import IsAdminOrOwnerOrReadOnly
from .serializers import NewsSerializer


class NewsListCreate(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


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
