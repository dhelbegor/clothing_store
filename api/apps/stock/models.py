import uuid

from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    CHILDISH = 'CHILDISH'
    ADULT = 'ADULT'
    CATEGORY_CHOICES = (
        (CHILDISH, 'Infantil'),
        (ADULT, 'Adulto')
    )
    P = 'P'
    M = 'M'
    G = 'G'
    GG = 'GG'
    SIZE_CHOICES = (
        (P, 'P'),
        (M, 'M'),
        (G, 'G'),
        (GG, 'GG')
    )
    sku = models.SlugField(_("SKU"), unique=True, blank=True, null=True)
    name = models.CharField(_('Nome'), max_length=100)
    image_url = models.CharField(_('Imagem'), max_length=355, null=True, blank=True)
    quantity = models.PositiveIntegerField(_('Quantidade'))
    category = models.CharField(_('Categoria'), max_length=8, choices=CATEGORY_CHOICES, default=CHILDISH)
    size = models.CharField(_('Tamanho'), max_length=2, choices=SIZE_CHOICES, default=P)
    price = models.DecimalField(_('Preço'), max_digits=13, decimal_places=8)

    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = slugify(uuid.uuid4())
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def sold_off(self):
        if self.quantity > 0:
            return False
        return True


class ProductManagement(models.Model):
    JANUARY = 'JANUARY'
    FEBRUARY = 'FEBRUARY'
    MARCH = 'MARCH'
    APRIL = 'APRIL'
    MAY = 'MAY'
    JUNE = 'JUNE'
    JULY = 'JULY'
    AUGUST = 'AUGUST'
    SEPTEMBER = 'SEPTEMBER'
    OCTOBER = 'OCTOBER'
    NOVEMBER = 'NOVEMBER'
    DECEMBER = 'DECEMBER'
    MONTH_CHOICES = (
        (JANUARY, 'Janeiro'),
        (FEBRUARY, 'Fevereiro'),
        (MARCH, 'Março'),
        (APRIL, 'Abril'),
        (MAY, 'Maio'),
        (JUNE, 'Junho'),
        (JULY, 'Julho'),
        (AUGUST, 'Agosto'),
        (SEPTEMBER, 'Setembro'),
        (OCTOBER, 'Outubro'),
        (NOVEMBER, 'Novembro'),
        (DECEMBER, 'Dezembro')
    )

    product = models.ForeignKey('stock.Product', verbose_name=_('Produto'), on_delete=models.PROTECT,
                                related_name='products')
    sell_per_day = models.IntegerField(_('Venda por dia'))
    total_sell = models.DecimalField(_('Total Vendido'), max_digits=13, decimal_places=8)
    month = models.CharField(_('Mês'), max_length=9, choices=MONTH_CHOICES, default=JANUARY)

    class Meta:
        verbose_name = _('Gerenciamento de produto')
        verbose_name_plural = _('Gerenciamento de produtos')

    def __str__(self):
        return self.product.name
