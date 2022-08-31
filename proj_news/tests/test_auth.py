from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class AuthTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        data = {
            "email": "init_user@gmail.com",
            "username": "init_user",
            "password": "user123456"
        }
        client = APIClient()
        client.post("/api/v1/token-auth/users/", data)

    def test_signup(self):
        data = {
            "email": "user@gmail.com",
            "username": "test_user",
            "password": "user123456"
        }
        response = self.client.post("/api/v1/token-auth/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_jwt(self):
        data = {
            "username": "init_user",
            "password": "user123456"
        }
        response = self.client.post("/api/v1/jwt-auth/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            "refresh": response.data['refresh']
        }
        response = self.client.post("/api/v1/jwt-auth/refresh/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

