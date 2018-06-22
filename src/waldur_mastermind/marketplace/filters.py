import django_filters

from waldur_core.core import filters as core_filters

from . import models


class ServiceProviderFilter(django_filters.FilterSet):
    customer = core_filters.URLFilter(view_name='customer-detail', name='customer__uuid')
    customer_uuid = django_filters.UUIDFilter(name='customer__uuid')

    class Meta(object):
        model = models.ServiceProvider
        fields = []


class ScreenshotstFilter(django_filters.FilterSet):
    o = django_filters.OrderingFilter(fields=(
        ('name', 'name'),
        ('description', 'description'),
        ('created', 'created'),
        ('modified', 'modified'),
    ))

    class Meta(object):
        model = models.Screenshots
        fields = []