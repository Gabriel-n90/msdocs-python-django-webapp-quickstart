from django.test import TestCase
from COM769-Python-Django-B00575451.models import MyModel

class MyModelTestCase(TestCase):
    def test_model_creation(self):
        obj = MyModel.objects.create(name='Test Name')
        self.assertEqual(obj.name, 'Test Name')
        # Add more assertions based on your model's behavior