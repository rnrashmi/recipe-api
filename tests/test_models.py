from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
  def Test_create_user_with_email_successful(self):
    email='chiku@yahoo.com'
    password='rashmi1234'
    user=get_user_model().objects.create_user(
      email=email,
      password=password
    )

    self.assertEqual(user.email,email)
    self.assertTrue(user,check_password(password))

  def new_user_email_normalized(self):
    email='test@yahoo.com'
    user=get_user_model().objects.create_user(
      email,'test123'
    )
    self.assertEqual(user.email,email.lower())

  def test_new_user_invalid_email(self):
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(None,'test1234')

  de test_new_superuser(self):
  user=get_user_model().objects.create_superuser(
    'test@yahoo.com',
    'rashmi1234'
  )

  self.assertTrue(user.is_superuser)
  self.assertTrue(user.is_staff)