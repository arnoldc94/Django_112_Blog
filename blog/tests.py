from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title="A test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.title}"
        self.assertEqual(expected_object_name, "A test")


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Another test")

    def test_homepage_uses_correct_model(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Another test")


    def test_view_url_exists_at_proper_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "blog_list.html")

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response,"blog_list.html" )
    

    def test_view_extends_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")


class DetailPageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Another test")

    def test_postdetail_uses_correct_model(self):
        response = self.client.get(reverse("blog_detail", args=[1]))
        self.assertContains(response, "Another test")

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get("/blogs/1/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("blog_detail", args=[1]))
        self.assertTemplateUsed(response, "blog_detail.html")

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("blog_detail", args=[1]))
        self.assertTemplateUsed(response,"blog_detail.html" )

    def test_view_extends_correct_template(self):
        response = self.client.get(reverse("blog_detail", args=[1]))
        self.assertTemplateUsed(response, "base.html")

    
