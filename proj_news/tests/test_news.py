from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from app_news.models import Category, News


class NewsTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser(username='init_n_user', email='init_user@gmail.com', password='user123456')

    def set_credentials(self):
        data = {
            "username": "init_n_user",
            "password": "user123456"
        }
        response = self.client.post("/api/v1/jwt-auth/", data)
        access = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access)

    def test_news_get(self):
        response = self.client.get("/api/v1/news/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_post(self):
        self.set_credentials()

        category = Category()
        category.name = 'test_category'
        category.save()

        data = {
            "title": "test_news",
            "content": "some content",
            "category": category.pk
        }
        response = self.client.post("/api/v1/news/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_news_by_id_get(self):
        self.set_credentials()

        news = News()
        news.title = 'test_news'
        news.content = 'some content'
        news.user = User.objects.get(username='init_n_user')
        news.save()

        response = self.client.get(f"/api/v1/news/{news.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_by_id_put(self):
        self.set_credentials()

        news = News()
        news.title = 'test_news'
        news.content = 'some content'
        news.user = User.objects.get(username='init_n_user')
        news.save()

        data = {
            "title": "edited_news",
            "content": "some content",
        }
        response = self.client.put(f"/api/v1/news/{news.pk}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_by_id_delete(self):
        self.set_credentials()

        news = News()
        news.title = 'test_news'
        news.content = 'some content'
        news.user = User.objects.get(username='init_n_user')
        news.save()

        response = self.client.delete(f"/api/v1/news/{news.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_news_by_category_get(self):
        response = self.client.get(f"/api/v1/news_by_category/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_by_user_get(self):
        response = self.client.get(f"/api/v1/news_by_user/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_get(self):
        response = self.client.get("/api/v1/news/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_post(self):
        self.set_credentials()

        data = {
            "name": "test_category"
        }
        response = self.client.post("/api/v1/category/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_category_by_id_get(self):
        category = Category()
        category.name = 'test_category'
        category.save()

        response = self.client.get(f"/api/v1/category/{category.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_by_id_put(self):
        self.set_credentials()

        category = Category()
        category.name = 'test_category'
        category.save()

        data = {
            "name": "edited_category"
        }
        response = self.client.put(f"/api/v1/category/{category.pk}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_by_id_delete(self):
        self.set_credentials()

        category = Category()
        category.name = 'test_category'
        category.save()

        response = self.client.delete(f"/api/v1/category/{category.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

