# test_personalized_greeting.py
import pytest
from personalized_greeting import greet

@pytest.mark.parametrize("input_name, expected_output", [
    ("Alice", "Hello Alice, welcome to computer programming."),
    ("Bob", "Hello Bob, welcome to computer programming."),
    ("Charlie", "Hello Charlie, welcome to computer programming.")
])
def test_personalized_greeting(capsys, input_name, expected_output):
    # Call the greet function with a test name
    greet(input_name)
    
    # Capture the output from the print statement
    captured = capsys.readouterr()  # Capture the output
    
    # Assert that the output is what we expect
    assert captured.out.strip() == expected_output
