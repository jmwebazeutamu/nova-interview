# test_personalized_greeting.py
import pytest

from personalized_greeting import greet

def test_personalized_greeting(capsys):  
    
    greet()
    
    # Capture the output from the print statement
    captured = capsys.readouterr()  # Capture the output
    
    # Assert that the output is what we expect. Adjust this based on the actual content.
    assert captured.out.strip() == "Hello Your Name Here, welcome to computer programming."
