from django.test import TestCase

# Create your tests here.
from .models import Book

class BookModelTest(TestCase):


	def setUp(cls):
		Book.objects.create(
		 title='Django',
		 subtitle='Flask',
		 author='Shaxzod',
		 isbn='999123124'
		)

	def test_title(self):
		book=Book.objects.get(id=1)
		expected_object_name=f'{book.title}'
		self.assertEquals(expected_object_name,'Django')
