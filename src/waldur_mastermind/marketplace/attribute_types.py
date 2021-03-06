from __future__ import unicode_literals

import six

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class AttributeType(object):
    @staticmethod
    def available_values_validate(values):
        if values:
            raise ValidationError(_('Available values must be empty for this attribute type.'))

    @staticmethod
    def validate(values, available_values):
        raise NotImplementedError


class BooleanAttribute(AttributeType):
    @staticmethod
    def validate(values, available_values=None):
        if not isinstance(values, bool):
            raise ValidationError(_('Value must be a boolean type  for this attribute type.'))


class StringAttribute(AttributeType):
    @staticmethod
    def validate(values, available_values=None):
        if not isinstance(values, six.text_type):
            raise ValidationError(_('Value must be a boolean type  for this attribute type.'))


class IntegerAttribute(AttributeType):
    @staticmethod
    def validate(values, available_values=None):
        if isinstance(values, bool) or not isinstance(values, int):
            raise ValidationError(_('Value must be an integer type  for this attribute type.'))


class ChoiceAttribute(AttributeType):
    @staticmethod
    def available_values_validate(values):
        if not values:
            raise ValidationError(_('Available values not must be empty for this attribute type.'))

        if not isinstance(values, list):
            raise ValidationError(_('Available values must be a list for this attribute type.'))

    @staticmethod
    def validate(values, available_values):
        if not isinstance(values, six.text_type):
            raise ValidationError(_('Value must be a string for this attribute.'))

        if not(values in available_values):
            raise ValidationError(_('This value is not available for this attribute.'))


class ListAttribute(AttributeType):
    @staticmethod
    def available_values_validate(values):
        if not values:
            raise ValidationError(_('Available values not must be empty for this attribute type.'))

        if not isinstance(values, list):
            raise ValidationError(_('Available values must be a list for this attribute type.'))

    @staticmethod
    def validate(values, available_values):
        if not isinstance(values, list):
            raise ValidationError(_('Value must be a list for this attribute.'))

        if not(set(values) <= set(available_values)):
            raise ValidationError(_('These values are not available for this attribute.'))


ATTRIBUTE_TYPES = (
    ('boolean', 'boolean'),
    ('string', 'string'),
    ('integer', 'integer'),
    ('choice', 'choice'),
    ('list', 'list'),
)


def get_attribute_type(name):
    attribute_type = {
        'boolean': BooleanAttribute,
        'string': StringAttribute,
        'integer': IntegerAttribute,
        'choice': ChoiceAttribute,
        'list': ListAttribute,
    }
    try:
        return attribute_type[name]
    except KeyError:
        pass
