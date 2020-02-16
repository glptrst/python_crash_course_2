import unittest

class Employee:
    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_raise(self, r=5_000):
        if r:
            self.salary = self.salary + r
        else:
            self.salary = self.salary + 5_000

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Rodrigo', 'Garcia', 60_000)
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 65_000)

    def test_give_custom_raise(self):
        self.employee.give_raise(7_000)
        self.assertEqual(self.employee.salary, 67_000)

if __name__ == '__main__':
    unittest.main()
