import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Runs once before any method"""
        print('setupClass\n')

    @classmethod
    def tearDownClass(cls):
        """Runs once after all methods"""
        print('\nteardownClass\n')

    def setUp(self):
        """setUp method runs before every single test"""
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        """tearDown method runs after every single test"""
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

    def test_fullname(self):
    	print('Test Fullname')
    	self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
    	self.assertEqual(self.emp_2.fullname, 'Sue Smith')


if __name__ == '__main__':
	unittest.main()