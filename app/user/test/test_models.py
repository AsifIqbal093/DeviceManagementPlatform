from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagerTests(TestCase):

    def test_create_user(self):
        """Test creating a new user."""
        email = 'test@example.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        """Test creating a new superuser."""
        email = 'superuser@example.com'
        password = 'superuserpassword'
        superuser = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertEqual(superuser.email, email)
        self.assertTrue(superuser.check_password(password))
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)


class AccountsModelTests(TestCase):

    def test_create_user(self):
        """Test creating a new user with email and password."""
        email = 'test@example.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.role, 'owner')

    def test_create_superuser(self):
        """Test creating a new superuser."""
        email = 'superuser@example.com'
        password = 'superuserpassword'
        superuser = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertEqual(superuser.email, email)
        self.assertTrue(superuser.check_password(password))
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertEqual(superuser.role, 'Lev Manager')

    def test_user_str(self):
        """Test the string representation of a user."""
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword',
            name='Test User'
        )
        self.assertEqual(str(user), user.name)
