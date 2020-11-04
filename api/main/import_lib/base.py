import csv
from decimal import Decimal


class Base:
    def __init__(self, filename):
        self.filename = filename

    def serializer(self):
        raise NotImplementedError('Should implement the "serializer" to parse method.')

    def get_file(self):
        return open(self.filename, 'r', encoding='latin1')


class ImportFromCSV(Base):
    def serializer(self):
        _file = self.get_file()
        reader = csv.DictReader(_file, delimiter=',')

        product = list()
        for col in reader:
            total_sell = (int(col['QT_SELL_PER_DAY']) * Decimal(col['PRICE']))
            product.append({'name': col['NAME'], 'quantity': col['QUANTITY'], 'size': col['SIZE'],
                            'category': col['CATEGORY'], 'price': col['PRICE'], 'image_url': col['URL'],
                            'sku': col['SKU'], 'sell_per_day': col['QT_SELL_PER_DAY'], 'month': col['MONTH'],
                            'total_sell': total_sell})
        _file.close()
        return product
