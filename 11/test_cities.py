import unittest
from city_functions import format_city

class CityTest(unittest.TestCase):

    def test_simple_case(self):
        result = format_city('roma', 'italia')
        self.assertEqual(result, 'Roma, Italia')

if __name__ == '__main__':
    unittest.main()
