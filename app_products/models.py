from django.db import models
from django.utils.translation import gettext_lazy as _

from app_common import models as common_model
from app_company import models as company_models


class ProductsModel(common_model.BaseModel):
    restaurant = models.ForeignKey(company_models.RestaurantModel, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Food')
        verbose_name_plural = _('Foods')


class ProductImageModel(common_model.BaseModel):
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
