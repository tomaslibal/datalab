import numpy as np
import hashlib
import math

class ImageHash():
    def hash(self, image_pixels):
        cells = 16
        w = len(image_pixels) # rows
        h = len(image_pixels[0]) # columns
        w_step = math.ceil(w / cells)
        h_step = math.ceil(h / cells)
        means = [[0 for i in range(cells)] for j in range(cells)]
        for i in range(0, w):
            for j in range(0, h):
                cell_i = math.floor(i / w_step)
                cell_j = math.floor(j / h_step)
                means[cell_i][cell_j] += float(image_pixels[i][j])

        means = np.array(means)
        num_pix_in_cell = w_step * h_step

        means //= float(num_pix_in_cell)

        means = means.flatten('F')

        h = hash(frozenset(means.tolist()))

        md5 = hashlib.md5((str(h).encode('utf-8')))

        return md5.hexdigest()