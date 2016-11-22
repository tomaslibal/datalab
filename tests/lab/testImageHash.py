from django.test import TestCase, RequestFactory

from lab.util.ImageHash import ImageHash

class SimpleTest(TestCase):
    def setUp(self):
        self.hasher = ImageHash()
        pass

    def test_hash_returns_string(self):
        hash = self.hasher.hash([[0, 0, 0, 0],[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(True, isinstance(hash, str))

    def test_hash_returns_non_empty_string(self):
        hash = self.hasher.hash([[0, 0, 0, 0],[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(True, len(hash) > 0)

    def test_two_different_inputs_return_different_hashes(self):
        hash = self.hasher.hash([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        hash2 = self.hasher.hash([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
        self.assertNotEqual(hash, hash2)