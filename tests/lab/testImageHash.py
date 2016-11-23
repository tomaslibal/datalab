from django.test import TestCase, RequestFactory
from PIL import Image

from lab.util.ImageHash import ImageHash

import distance

def get_r_pixels(path = 'tests/resources/test_panda.jpg'):
    w = 96
    h = 96
    img = Image.open(path)
    img.thumbnail((w, h), Image.ANTIALIAS)
    pxs = list(img.getdata())
    res = [[0 for i in range(w)] for j in range(h)]
    for i in range(w):
        for j in range(h):
            res[i][j] = pxs[i*j][0]
    return res

class SimpleTest(TestCase):
    def setUp(self):
        self.hasher = ImageHash()
        self.pixels = get_r_pixels()
        pass

    def test_hash_returns_string(self):
        hash = self.hasher.hash(self.pixels)
        self.assertEqual(True, isinstance(hash, str))

    def test_hash_returns_non_empty_string(self):
        hash = self.hasher.hash(self.pixels)
        self.assertEqual(True, len(hash) > 0)

    def test_two_same_images_return_same_hash(self):
        hash = self.hasher.hash(get_r_pixels('tests/resources/test_cloud.jpg'))
        hash2 = self.hasher.hash(get_r_pixels('tests/resources/test_cloud.jpg'))
        self.assertEqual(hash, hash2)

    def test_two_different_inputs_return_different_hashes(self):
        hash = self.hasher.hash(get_r_pixels('tests/resources/test_cloud.jpg'))
        hash2 = self.hasher.hash(get_r_pixels('tests/resources/test_cloud_2.jpg'))
        self.assertNotEqual(hash, hash2)