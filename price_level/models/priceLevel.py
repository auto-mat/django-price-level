"""Price level model."""
from author.decorators import with_author

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


@with_author
class PriceLevel(TimeStampedModel, models.Model):
    """Stores price levels."""

    pricable = models.ForeignKey(
        settings.PRICE_LEVEL_MODEL,
        verbose_name=_("Priceable"),
        on_delete=models.CASCADE,
    )
    @property
    def priceable(self):
        return self.pricable
    @priceable.setter
    def priceable(self, v):
        self.pricable = v

    award_level = models.ForeignKey(
        'AwardLevel',
        default=None,
        null=True,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=127,
    )
    price = models.FloatField(
        verbose_name=_("Price"),
        validators=[
            MinValueValidator(1),
        ],
        default=100,
    )
    category = models.CharField(
        verbose_name=_("Category"),
        max_length=20,
        choices=settings.PRICE_LEVEL_CATEGORY_CHOICES,
        default=settings.PRICE_LEVEL_CATEGORY_DEFAULT,
    )
    takes_effect_on = models.DateTimeField(
        verbose_name=_("Date, when this takes effect"),
    )
    offer_ends = models.DateTimeField(
        verbose_name=_("Date/time when the price level is no longer available."),
        null=True,
        blank=True,
    )

    def __str__(self):
        """Return name as string representation."""
        return self.name
