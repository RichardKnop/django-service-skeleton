from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.user.service import UserService


class RegisterTestCase(TestCase):
    def setUp(self):
        self.service = UserService()

    def test_register_invalid_email(self):
        with self.assertRaises(ValidationError) as context:
            self.service.register('invalid e-mail address', 'password')

        self.assertEqual(context.exception.message_dict['email'][0],
                         'Enter a valid email address.')

    def test_register(self):
        self.service.register('foo@example.com', 'password')

    def test_register_taken_email(self):
        self.service.register('foo@example.com', 'password')

        with self.assertRaises(ValidationError) as context:
            self.service.register('Foo@examplE.com', 'password')

        self.assertEqual(context.exception.message_dict['__all__'][0],
                         'Email not unique')