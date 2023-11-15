from django.test import TestCase
from COM769-Python-Django-B00575451.forms import MyForm  # Replace 'myapp' with the actual name of your app

class FormsTestCase(TestCase):
    def test_valid_form(self):
        form_data = {'field1': 'value1', 'field2': 'value2'}  # Replace with actual form field values
        form = MyForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'field1': '', 'field2': 'value2'}  # Invalid data, adjust as needed
        form = MyForm(data=form_data)
        self.assertFalse(form.is_valid())
