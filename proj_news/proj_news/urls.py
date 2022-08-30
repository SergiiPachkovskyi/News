"""proj_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from app_news.views import NewsListCreate, NewsRetrieveUpdateDestroy, NewsByCategoryRetrieve, NewsByUserRetrieve

urlpatterns = [
    path('admin/', admin.site.urls),

    # news
    path('api/v1/news/', NewsListCreate.as_view()),
    path('api/v1/news/<int:pk>/', NewsRetrieveUpdateDestroy.as_view()),
    path('api/v1/news_by_category/<int:cat_id>/', NewsByCategoryRetrieve.as_view()),
    path('api/v1/news_by_user/<int:user_id>/', NewsByUserRetrieve.as_view()),

    # session-based auth
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    # jwt auth
    path('api/v1/jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/jwt/refresh/verify', TokenVerifyView.as_view(), name='token_verify'),
]
