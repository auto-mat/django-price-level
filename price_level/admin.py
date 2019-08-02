from django.contrib import admin

from . import models


@admin.register(models.PriceLevel)
class PriceLevelAdmin(admin.ModelAdmin):
    """Admin model for PriceLevels."""

    list_display = ('name', 'award_level', 'pricable', 'price', 'category', 'takes_effect_on')
    list_filter = ('pricable', 'category')
    readonly_fields = (
        'author',
        'updated_by',
    )


@admin.register(models.AwardLevel)
class AwardLevelAdmin(admin.ModelAdmin):
    """Admin model for AwardLevels."""

    list_display = ('name', 'category')
    list_filter = ('category',)
    readonly_fields = (
        'author',
        'updated_by',
    )

