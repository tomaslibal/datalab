from PIL import Image

from lab.models import Datapoint, Label, UserDefinedEntity

class ImageEntityProcessor():
    @staticmethod
    def process(path, labels, entity, width=96, height=96):
        img = Image.open(path)
        img = img.resize((width, height), resample=Image.BILINEAR)
        p = list(img.getdata())
        # extract just the red compoment for now:
        pixels_str = ','.join(str(px[0]) for px in p)

        dp = Datapoint(entity_type=entity, name="Imported", data=pixels_str, description="")
        dp.save()

        for label in labels:
            if len(label) > 0:
                obj, created = Label.objects.get_or_create(
                    name=label
                )
                dp.labels.add(obj)

        dp.save()

        return [dp]

    @staticmethod
    def out(entity):
        pass