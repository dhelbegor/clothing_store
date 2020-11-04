from .base import ImportFromCSV


class ImportFactory:
    @staticmethod
    def get_csv(filename):
        _file = ImportFromCSV(filename)
        return _file.serializer()
