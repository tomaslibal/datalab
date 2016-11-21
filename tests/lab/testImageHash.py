from django.test import TestCase, RequestFactory

from lab.util.ImageHash import ImageHash

class SimpleTest(TestCase):
    def setUp(self):
        self.hasher = ImageHash()
        pass

    def test_hash_returns_string(self):
        hash = self.hasher.hash()
        self.assertEqual(True, isinstance(hash, str))