"""Award level model."""
from author.decorators import with_author

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


@with_author
class AwardLevel(TimeStampedModel, models.Model):
    """Stores award levels."""

    priceable = models.ForeignKey(
        settings.PRICE_LEVEL_MODEL,
        verbose_name=_("Priceable"),
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=127,
    )
    description_html = models.TextField(
        verbose_name=_("HTML description")
    )
    category = models.CharField(
        verbose_name=_("Category"),
        max_length=60,
        choices=settings.AWARD_LEVEL_CATEGORY_CHOICES,
        default=settings.AWARD_LEVEL_CATEGORY_DEFAULT,
    )


    def __str__(self):
        """Return name as string representation."""
        return self.name
