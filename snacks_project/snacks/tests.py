from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse


class SnacksTests(SimpleTestCase):
    def test_home_page(self):
        url = reverse("home")
        response=self.client.get(url).status_code
        self.assertEqual(response, 200)
    
    def test_home_page_template(self):
        url = reverse("home")
        response=self.client.get(url)
        self.assertTemplateUsed(response,"home.html")  

    def test_about(self):
        url = reverse("about")
        response = self.client.get(url).status_code
        self.assertEqual(response, 200) 

    def test_about_template(self):
        url = reverse("about")
        response=self.client.get(url)
        self.assertTemplateUsed(response,"about.html")       


