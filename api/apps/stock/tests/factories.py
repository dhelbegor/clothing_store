import factory
import factory.fuzzy
from apps.stock.models import Product, ProductManagement

CATEGORY = [x[0] for x in Product.CATEGORY_CHOICES]
SIZE = [x[0] for x in Product.SIZE_CHOICES]
MONTH = [x[0] for x in ProductManagement.MONTH_CHOICES]


class ProductFactory(factory.django.DjangoModelFactory):
    name = "Camiseta Mr Kitsch Logo Branca/Preta"
    sku = factory.Faker('random_int', min=1, max=10000)
    category = factory.fuzzy.FuzzyChoice(CATEGORY)
    size = factory.fuzzy.FuzzyChoice(SIZE)
    image_url = factory.LazyAttribute(lambda o: f'product/{o.name}')
    quantity = factory.fuzzy.FuzzyInteger(100000)
    price = factory.fuzzy.FuzzyDecimal(low=1000)

    class Meta:
        model = Product
        django_get_or_create = ('sku',)


class ProductManagementFactory(factory.django.DjangoModelFactory):
    product = factory.SubFactory(ProductFactory)
    total_sell = factory.fuzzy.FuzzyDecimal(low=1000)
    sell_per_day = factory.Faker('random_int', min=1, max=10000)
    month = factory.fuzzy.FuzzyChoice(MONTH)

    class Meta:
        model = ProductManagement
