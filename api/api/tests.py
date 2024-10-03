from http.client import responses

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class TeammateTest(APITestCase):

    def setUp(self):
        data = {
            "first_name": "Albert",
            "last_name": "Einstein",
            "email": "aeinstein@horror.me",
            "team": ""
        }

        self.client.post(reverse("teammate-list"), data)

    def test_create_teammate(self):

        data = {
            "first_name" : "Gilbert",
            "last_name" : "McGoover",
            "email" : "gilmcgoover@horror.me",
            "team" : ""
        }

        response = self.client.post(reverse("teammate-list"), data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_get_teammates(self):

        response = self.client.get(reverse("teammate-list"))
        self.assertEquals(response.status_code, status.HTTP_200_OK)


