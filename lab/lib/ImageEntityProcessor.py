from PIL import Image

class ImageEntityProcessor():
    @staticmethod
    def process(path, width=96, height=96):
        img = Image.open(path)
        img = img.resize((width, height), resample=Image.BILINEAR)
        p = list(img.getdata())
        # extract just the red compoment for now:
        pixels_str = ','.join(str(px[0]) for px in p)
        return pixels_str, width, height

    @staticmethod
    def out(entity):
        pass