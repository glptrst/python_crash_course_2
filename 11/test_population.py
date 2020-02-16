import unittest
from population import format_city

class CityTest(unittest.TestCase):

    def test_simple_case(self):
        result = format_city('roma', 'italia')
        self.assertEqual(result, 'Roma, Italia')

    def test_population_case(self):
        result = format_city('roma', 'italia', 2_873_000)
        self.assertEqual(result, 'Roma, Italia -- population 2873000')

if __name__ == '__main__':
    unittest.main()
