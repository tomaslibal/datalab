class GenericEntityProcessor():
    @staticmethod
    def process(path):
        with open(path, 'r') as data_file:
            return data_file.read()

    @staticmethod
    def out(entity):
        pass