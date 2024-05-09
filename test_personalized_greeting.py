# test_personalized_greeting.py
import unittest
from io import StringIO
import sys

# Import the script to test
import personalized_greeting

class TestPersonalizedGreeting(unittest.TestCase):
    def test_output(self):
        # Redirect stdout to capture print statements
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        
        # Running the function from personalized_greeting.py
        personalized_greeting.myname = "Test Name"  # Overriding the myname variable for testing
        personalized_greeting.print(f"Hello {personalized_greeting.myname}, welcome to computer programming.")
        
        # Reset redirect.
        sys.stdout = sys.__stdout__
        
        # Check if the output is correct
        self.assertEqual(capturedOutput.getvalue().strip(), "Hello Test Name, welcome to computer programming.")

if __name__ == '__main__':
    unittest.main()
