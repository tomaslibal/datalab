from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from lab.views import home

class ViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='foo', email='foo@example.com', password='bar')

    def test_home(self):
        # Create an instance of a GET request.
        request = self.factory.get('/')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        # request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = home(request)
        # Use this syntax for class-based views.
        # response = MyView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_label_detail(self):
        pass