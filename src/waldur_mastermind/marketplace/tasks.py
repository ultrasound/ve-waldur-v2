from __future__ import unicode_literals

import logging

from celery import shared_task
from django.conf import settings

from waldur_core.core import utils as core_utils

from . import utils, models, plugins

logger = logging.getLogger(__name__)


@shared_task(name='marketplace.process_order')
def process_order(serialized_order, serialized_user):
    order = core_utils.deserialize_instance(serialized_order)
    user = core_utils.deserialize_instance(serialized_user)
    for item in order.items.all():
        plugins.manager.process(item, user)


@shared_task(name='marketplace.create_screenshot_thumbnail')
def create_screenshot_thumbnail(uuid):
    screenshot = models.Screenshot.objects.get(uuid=uuid)
    utils.create_screenshot_thumbnail(screenshot)


@shared_task(name='marketplace.notify_order_approvers')
def notify_order_approvers(uuid):
    order = models.Order.objects.get(uuid=uuid)
    users = order.get_approvers()
    emails = [u.email for u in users if u.email]

    context = {
        'order_url': settings.ORDER_LINK_TEMPLATE.format(order=order),
        'order': order,
        'site_name': settings.WALDUR_CORE['SITE_NAME'],
    }

    core_utils.broadcast_mail('marketplace', 'notification_approval', context, emails)
