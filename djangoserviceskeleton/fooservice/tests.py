from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import User
from .password import *


class UserTestCase(TestCase):
    def test_password_hashing(self):
        user = User(
            email='foo@example.com',
            password='password',
        )
        user.save()

        # Check that password is converted to a hash upon saving
        self.assertTrue(check('password', user.password))

        # Check that password is not hashed again when its value did not change
        user.save()
        self.assertTrue(check('password', user.password))

        # Check that password is hashed again when its value changed
        user.password = '$this_is_my_new_password'
        user.save()
        self.assertFalse(check('password', user.password))
        self.assertTrue(check('$this_is_my_new_password', user.password))

    def test_email_case_insensivity(self):
        u1 = User(
            email='test@justyoyo.com',
            password='password',
        )
        u1.save()

        with self.assertRaises(ValidationError) as context:
            u2 = User(
                email='TesT@justyoyo.com',
                password='password',
            )
            u2.full_clean()

        self.assertEqual(str(context.exception.message_dict['__all__'][0]), 'Email not unique')