# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^PriceLevel/~create/$",
        view=views.PriceLevelCreateView.as_view(),
        name='PriceLevel_create',
    ),
    url(
        regex="^PriceLevel/(?P<pk>\d+)/~delete/$",
        view=views.PriceLevelDeleteView.as_view(),
        name='PriceLevel_delete',
    ),
    url(
        regex="^PriceLevel/(?P<pk>\d+)/$",
        view=views.PriceLevelDetailView.as_view(),
        name='PriceLevel_detail',
    ),
    url(
        regex="^PriceLevel/(?P<pk>\d+)/~update/$",
        view=views.PriceLevelUpdateView.as_view(),
        name='PriceLevel_update',
    ),
    url(
        regex="^PriceLevel/$",
        view=views.PriceLevelListView.as_view(),
        name='PriceLevel_list',
    ),
	]
