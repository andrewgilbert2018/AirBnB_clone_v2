#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Test for user class"""

    def __init__(self, *args, **kwargs):
        """initialize test """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ test with first name"""
        new = self.value()
        self.assertEqual(new.first_name, None)

    def test_last_name(self):
        """ test with last name """
        new = self.value()
        self.assertEqual(new.last_name, None)

    def test_email(self):
        """test email """
        new = self.value()
        self.assertEqual(new.email, None)

    def test_password(self):
        """test password """
        new = self.value()
        self.assertEqual(new.password, None)
