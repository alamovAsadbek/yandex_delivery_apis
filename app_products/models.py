from django.db import models
from django.utils.translation import gettext_lazy as _


class Foods(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return _(self.name)

    class Meta:
        verbose_name = _('Food')
        verbose_name_plural = _('Foods')
