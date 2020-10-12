import unittest


class AlmostIncreaseSequence(unittest.TestCase):
    
    def test_input_case_1_should_be_return_false(self):
        list_of_number = [1, 3, 2, 1]
        
        expected = False
        actual = almostIncreaseSequence(list_of_number)
        
        self.assertEqual(actual, expected)

def almostIncreaseSequence(list_of_number):
        return True

unittest.main()
