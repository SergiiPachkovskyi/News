from rest_framework import serializers

from .models import News, Category


class NewsSerializer(serializers.ModelSerializer):
    """
        Serializer for class News
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = News
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
        Serializer for class Category
    """

    class Meta:
        model = Category
        fields = '__all__'

