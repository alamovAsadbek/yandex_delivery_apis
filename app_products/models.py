from django.db import models
from django.utils.translation import gettext_lazy as _

from app_company import models as company_models


class ProductsModel(models.Model):
    restaurant = models.ForeignKey(company_models.RestaurantModel, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return _(self.name)

    class Meta:
        verbose_name = _('Food')
        verbose_name_plural = _('Foods')


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
