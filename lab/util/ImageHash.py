import numpy as np
import math

class ImageHash():
    def median(self, arr):
        return np.median(arr)

    def print_as_ascii(self, bits, cols, rows):
        return np.array(bits).reshape(cols, rows)

    def to_bits(self, means, image_pixels, cells):
        w = len(image_pixels)  # rows
        h = len(image_pixels[0])  # columns

        w_step = math.ceil(w / cells)
        h_step = math.ceil(h / cells)

        HALF = (w_step * h_step) / 2

        num_above = [[0 for i in range(cells)] for j in range(cells)]
        bits = [[0 for i in range(cells)] for j in range(cells)]

        for i in range(0, w):
            for j in range(0, h):
                cell_i = math.floor(i / w_step)
                cell_j = math.floor(j / h_step)
                if int(image_pixels[i][j]) > int(means[cell_i][cell_j]):
                    num_above[cell_i][cell_j] += 1

        idx = 0
        num_above = np.array(num_above).flatten('F')
        bits = np.array(bits).flatten('F')

        for above in num_above:
            if above > HALF:
                bits[idx] = 1
            idx += 1

        return bits

    def to_hex(self, bits_array):
        return '{0:0={b}x}'.format(int(''.join([str(x) for x in bits_array]), 2), b=len(bits_array) // 4)

    def hash(self, image_pixels, cells = 16):
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

        means //= num_pix_in_cell

        bits = self.to_bits(means, image_pixels, cells)

        return self.to_hex(bits)