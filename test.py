from main import *

def test_hello_test():
    assert hello()=='Hello FastAPI'

def test_isPrime_test():
    assert is_prime(2)==True

def test_fibonacci_test():
    assert fibonacci(1)==1
