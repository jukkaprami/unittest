# This modulc contains tests for module "moduletotest.py"

# Libraries and modules
import unittest # Module for test
import moduletotest # Module to be tested

# Test classes

class Cluetest(unittest.TestCase):

    def test_updateclue(self):
        clue = list('?????')
        secret_word = 'sorsa'
        guessed_word = 'sorsa'
        result = moduletotest.update_clue(guessed_word, secret_word, clue)
        expected_result = list('s??s?')
        self.assertEqual(result, expected_result)

    def test_update_clue2(self):
        clue = list('?????')
        secret_word = 'sorsa'
        guessed_word = 'o'
        result = moduletotest.update_clue(guessed_word, secret_word, clue)
        expected_result = list('?o???')
        self.assertEqual(result, expected_result)
                       

if __name__ == "__main__":
    unittest.main()
    