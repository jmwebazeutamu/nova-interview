import hello  # This imports the greeting function from the hello.py file

def test_greeting():
    assert hello.greeting() == "Hello, welcome to programming", "Test failed: The greeting function did not return the expected message."
