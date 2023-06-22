""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'file')
class test_basemodel(unittest.TestCase):
    """ """
    maxDiff = None

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        dictionary = {}
        dictionary.update(i.__dict__)
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         dictionary))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertTrue("Name" in new.__dict__)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_delete(self):
        """Test delete """
        new = self.value()
        new.save()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        new.delete()
        self.assertEqual(type(new.updated_at), datetime.datetime)

    def test_dict(self):
        """Test creating with dict """
        kwargs = {'name': "California"}
        new = self.value(**kwargs)
        new.save()
        self.assertTrue("name" in new.__dict__)

    def test_no_weirdkeys(self):
        """Test that not weird keys are created """
        new = self.value()
        new.save()
        self.assertTrue("_sa_instance_state" not in new.to_dict())
