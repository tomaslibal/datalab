from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from lab.views import home, label_delete
from lab.models import Label

class LabelTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='foo', email='foo@example.com', password='bar')

    def test_delete_path(self):
        # setup a label
        testLabel = Label(name='foo', description='bar')
        testLabel.save()
        id = testLabel.id

        self.assertEqual(1, Label.objects.filter(name='foo').count())

        # act
        request = self.factory.get('/api/label/' + str(id)  + '/delete')
        request.user = AnonymousUser()
        response = label_delete(request, id)

        # assert
        self.assertEqual(0, Label.objects.filter(name='foo').count())