from ddt import ddt, data
import mock
from rest_framework import status

from waldur_mastermind.support import models, tasks
from waldur_mastermind.support.tests.base import override_support_settings

from . import factories, base


@ddt
class SupportUserRetrieveTest(base.BaseTest):

    def setUp(self):
        super(SupportUserRetrieveTest, self).setUp()
        self.support_user = factories.SupportUserFactory()

    @data('staff', 'global_support')
    def test_staff_or_support_can_retrieve_support_users(self, user):
        self.client.force_authenticate(getattr(self.fixture, user))

        response = self.client.get(factories.SupportUserFactory.get_list_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['uuid'], self.support_user.uuid.hex)

    @data('user')
    def test_user_can_not_retrieve_support_users(self, user):
        self.client.force_authenticate(getattr(self.fixture, user))

        response = self.client.get(factories.SupportUserFactory.get_list_url())
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymouse_user_can_not_retrieve_support_users(self):
        response = self.client.get(factories.SupportUserFactory.get_list_url())
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @override_support_settings(ENABLED=False)
    def test_user_can_not_retrieve_support_users_if_support_extension_is_disabled(self):
        self.client.force_authenticate(self.fixture.staff)
        response = self.client.get(factories.SupportUserFactory.get_list_url())
        self.assertEqual(response.status_code, status.HTTP_424_FAILED_DEPENDENCY)


@override_support_settings(ENABLED=True)
@mock.patch('waldur_mastermind.support.backend.get_active_backend')
class SupportUserPullTest(base.BaseTest):
    def test_if_user_is_not_available_he_is_marked_as_disabled(self, mocked_backend):
        # Arrange
        mocked_backend().get_users.return_value = [
            models.SupportUser(backend_id='alice'),
        ]
        alice = factories.SupportUserFactory(backend_id='alice')
        bob = factories.SupportUserFactory(backend_id='bob')

        # Act
        tasks.SupportUserPullTask().run()

        # Assert
        alice.refresh_from_db()
        bob.refresh_from_db()
        self.assertTrue(alice.is_active)
        self.assertFalse(bob.is_active)

    def test_if_user_is_available_he_is_marked_as_enabled(self, mocked_backend):
        # Arrange
        mocked_backend().get_users.return_value = [
            models.SupportUser(backend_id='alice'),
        ]
        alice = factories.SupportUserFactory(backend_id='alice', is_active=False)

        # Act
        tasks.SupportUserPullTask().run()

        # Assert
        alice.refresh_from_db()
        self.assertTrue(alice.is_active)
