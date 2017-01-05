# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	PriceLevel,
)


class PriceLevelCreateView(CreateView):

    model = PriceLevel


class PriceLevelDeleteView(DeleteView):

    model = PriceLevel


class PriceLevelDetailView(DetailView):

    model = PriceLevel


class PriceLevelUpdateView(UpdateView):

    model = PriceLevel


class PriceLevelListView(ListView):

    model = PriceLevel

