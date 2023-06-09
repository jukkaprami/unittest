# For testing the timetools module

# Libraeries and modules
import unittest
import timetools

# Test classes
class test_time(unittest.TestCase):

    def test_datediff(self):
        expected_result = (3, 'days')
        result = timetools.datediff('2023-06-09', '2023-06-06')
        self.assertEqual(result, expected_result)

    def test_timediff2(self):
        result = timetools.timediff2('18:00:00', '23:30:00', 'minute')
        expected_result = (330)
        self.assertEqual(result, expected_result)

    def test_timediff4(self):
        result = timetools.timediff2('18:00:00', '23:30:00', 'second')
        expected_result = (19800)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()