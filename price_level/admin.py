from django.contrib import admin

from . import models


@admin.register(models.PriceLevel)
class PriceLevelAdmin(admin.ModelAdmin):
    """Admin model for PriceLevels."""

    list_display = ('name', 'priceable', 'price', 'category', 'takes_effect_on', 'offer_ends')
    list_filter = ('priceable', 'category')
