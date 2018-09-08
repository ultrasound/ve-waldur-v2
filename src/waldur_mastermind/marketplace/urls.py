from __future__ import unicode_literals

from django.conf.urls import url

from waldur_mastermind.marketplace import views


def register_in(router):
    router.register(r'marketplace-service-providers', views.ServiceProviderViewSet,
                    base_name='marketplace-service-provider'),
    router.register(r'marketplace-categories', views.CategoryViewSet,
                    base_name='marketplace-category'),
    router.register(r'marketplace-offerings', views.OfferingViewSet,
                    base_name='marketplace-offering')
    router.register(r'marketplace-plans', views.PlanViewSet,
                    base_name='marketplace-plan')
    router.register(r'marketplace-screenshots', views.ScreenshotViewSet,
                    base_name='marketplace-screenshot')
    router.register(r'marketplace-orders', views.OrderViewSet,
                    base_name='marketplace-order'),


urlpatterns = [
    url(r'^api/customers/(?P<uuid>[^/.]+)/offerings/$', views.CustomerOfferingViewSet.as_view()),
]
