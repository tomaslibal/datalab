from lab.models import Datapoint, Label, UserDefinedEntity

class GenericEntityProcessor():
    @staticmethod
    def process(path, labels, entity):
        with open(path, 'r') as data_file:
            lines = data_file.readlines()
            dpts = []

            for line in lines:
                print("saving " + entity.entity_type + " dp=" + line)
                dp = Datapoint(entity_type=entity, name="Imported", data=line, description="")
                dp.save()

                for label in labels:
                    if len(label) > 0:
                        obj, created = Label.objects.get_or_create(
                            name=label
                        )
                        dp.labels.add(obj)

                dp.save()
                dpts.append(dp)

            return dpts

    @staticmethod
    def out(entity):
        pass