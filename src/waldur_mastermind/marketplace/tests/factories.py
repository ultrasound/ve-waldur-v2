import factory
from django.db.models import signals
from rest_framework.reverse import reverse

from waldur_core.structure.tests import factories as structure_factories

from .. import models


class ServiceProviderFactory(factory.DjangoModelFactory):
    class Meta(object):
        model = models.ServiceProvider

    customer = factory.SubFactory(structure_factories.CustomerFactory)

    @classmethod
    def get_url(cls, service_provider=None, action=None):
        if service_provider is None:
            service_provider = ServiceProviderFactory()
        url = 'http://testserver' + reverse('marketplace-service-provider-detail',
                                            kwargs={'uuid': service_provider.uuid})
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls, action=None):
        url = 'http://testserver' + reverse('marketplace-service-provider-list')
        return url if action is None else url + action + '/'


class CategoryFactory(factory.DjangoModelFactory):
    class Meta(object):
        model = models.Category

    title = factory.Sequence(lambda n: 'category-%s' % n)

    @classmethod
    def get_url(cls, category=None, action=None):
        if category is None:
            category = CategoryFactory()
        url = 'http://testserver' + reverse('marketplace-category-detail',
                                            kwargs={'uuid': category.uuid})
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls, action=None):
        url = 'http://testserver' + reverse('marketplace-category-list')
        return url if action is None else url + action + '/'


class OfferingFactory(factory.DjangoModelFactory):
    class Meta(object):
        model = models.Offering

    name = factory.Sequence(lambda n: 'offering-%s' % n)
    category = factory.SubFactory(CategoryFactory)
    provider = factory.SubFactory(ServiceProviderFactory)

    @classmethod
    def get_url(cls, offering=None, action=None):
        if offering is None:
            offering = OfferingFactory()
        url = 'http://testserver' + reverse('marketplace-offering-detail',
                                            kwargs={'uuid': offering.uuid})
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls, action=None):
        url = 'http://testserver' + reverse('marketplace-offering-list')
        return url if action is None else url + action + '/'


class SectionFactory(factory.DjangoModelFactory):
    class Meta(object):
        model = models.Section

    key = factory.Sequence(lambda n: 'section-%s' % n)
    category = factory.SubFactory(CategoryFactory)


class AttributesFactory(factory.DjangoModelFactory):
    class Meta(object):
        model = models.Attribute

    key = factory.Sequence(lambda n: 'attribute-%s' % n)
    section = factory.SubFactory(SectionFactory)
    type = 'list'
    available_values = ["web_chat", "phone"]


@factory.django.mute_signals(signals.pre_save, signals.post_save)
class ScreenshotsFactory(factory.DjangoModelFactory):
    class Meta(object):
        model = models.Screenshots

    name = factory.Sequence(lambda n: 'screenshot-%s' % n)
    image = factory.django.ImageField()
    offering = factory.SubFactory(OfferingFactory)

    @classmethod
    def get_url(cls, screenshot=None, action=None):
        if screenshot is None:
            screenshot = ScreenshotsFactory()
        url = 'http://testserver' + reverse('marketplace-screenshot-detail',
                                            kwargs={'uuid': screenshot.uuid})
        return url if action is None else url + action + '/'

    @classmethod
    def get_list_url(cls, action=None):
        url = 'http://testserver' + reverse('marketplace-screenshot-list')
        return url if action is None else url + action + '/'