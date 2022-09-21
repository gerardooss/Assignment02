from http import client
from multiprocessing.connection import Client
from unittest import result
from urllib import response
from django.test import TestCase, Client
from mywatchlist.models import *
from django.urls import reverse

# Create your tests here.
class MauTes(TestCase):
    def test_html(self):
        client = Client()
        result = client.get(reverse("mywatchlist:show_html"))
        self.assertEquals(result.status_code, 200)

    def test_xml(self):
        client = Client()
        result = client.get(reverse("mywatchlist:show_xml"))
        self.assertEquals(result.status_code, 200)
        
    def test_json(self):
        client = Client()
        result = client.get(reverse("mywatchlist:show_json"))
        self.assertEquals(result.status_code, 200)