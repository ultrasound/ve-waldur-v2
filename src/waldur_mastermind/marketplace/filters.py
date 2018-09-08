import json

from django.db.models import Q
import django_filters
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions as rf_exceptions
from rest_framework.filters import DjangoFilterBackend

from waldur_core.core import filters as core_filters
from waldur_core.structure import models as structure_models

from . import models


class ServiceProviderFilter(django_filters.FilterSet):
    customer = core_filters.URLFilter(view_name='customer-detail', name='customer__uuid')
    customer_uuid = django_filters.UUIDFilter(name='customer__uuid')

    class Meta(object):
        model = models.ServiceProvider
        fields = []


class OfferingFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    customer = core_filters.URLFilter(view_name='customer-detail', name='customer__uuid')
    customer_uuid = django_filters.UUIDFilter(name='customer__uuid')
    attributes = django_filters.CharFilter(name='attributes', method='filter_attributes')
    state = core_filters.MappedMultipleChoiceFilter(
        choices=[(representation, representation) for db_value, representation in models.Offering.States.CHOICES],
        choice_mappings={representation: db_value for db_value, representation in models.Offering.States.CHOICES},
    )
    category_uuid = django_filters.UUIDFilter(name='category__uuid')

    def filter_attributes(self, queryset, name, value):
        try:
            value = json.loads(value)
        except ValueError:
            raise rf_exceptions.ValidationError(_('Filter attribute is not valid json.'))

        if not isinstance(value, dict):
            raise rf_exceptions.ValidationError(_('Filter attribute should be an dict.'))

        for k, v in value.items():
            if isinstance(v, list):
                # If a filter value is a list, use multiple choice.
                queryset = queryset.filter(**{'attributes__{key}__has_any_keys'.format(key=k): v})
            else:
                queryset = queryset.filter(attributes__contains={k: v})
        return queryset

    class Meta(object):
        model = models.Offering
        fields = ['shared', 'type']


class OfferingCustomersFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.user

        if not user.is_staff and not user.is_support:
            connected_customers = set(structure_models.Customer.objects.all().filter(
                Q(permissions__user=user, permissions__is_active=True) |
                Q(projects__permissions__user=user, projects__permissions__is_active=True)
            ).distinct())
            queryset = queryset.filter(
                Q(shared=True) |
                Q(shared=False, allowed_customers__in=connected_customers) |
                Q(shared=False, customer__in=connected_customers)
            )
        return queryset


class ScreenshotFilter(django_filters.FilterSet):
    offering = core_filters.URLFilter(view_name='marketplace-offering-detail', name='offering__uuid')
    offering_uuid = django_filters.UUIDFilter(name='offering__uuid')

    o = django_filters.OrderingFilter(fields=('name', 'created'))

    class Meta(object):
        model = models.Screenshot
        fields = []


class OrderFilter(django_filters.FilterSet):
    project = core_filters.URLFilter(view_name='project-detail', name='project__uuid')
    project_uuid = django_filters.UUIDFilter(name='project__uuid')

    o = django_filters.OrderingFilter(fields=('created', 'approved_at', 'total_cost', 'state'))

    class Meta(object):
        model = models.Order
        fields = ['state']


class ItemFilter(django_filters.FilterSet):
    offering = core_filters.URLFilter(view_name='marketplace-offering-detail', name='offering__uuid')
    offering_uuid = django_filters.UUIDFilter(name='offering__uuid')

    order = core_filters.URLFilter(view_name='marketplace-order-detail', name='order__uuid')
    order_uuid = django_filters.UUIDFilter(name='order__uuid')

    class Meta(object):
        model = models.OrderItem
        fields = []


class PlanFilter(django_filters.FilterSet):
    offering = core_filters.URLFilter(view_name='marketplace-offering-detail', name='offering__uuid')
    offering_uuid = django_filters.UUIDFilter(name='offering__uuid')

    class Meta(object):
        model = models.Plan
        fields = []
