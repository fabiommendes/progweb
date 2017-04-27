from fib import fib
import unittest
import pytest


class TestFib(unittest.TestCase):
    def setUp(self):
        self.x = 5
        self.fx = 8

    def tearDown(self):
        pass

    def test_other_fib(self):
        self.assertEqual(fib(self.x), self.fx)
        
    def test_knwon_fibs(self):
        print('hello world')
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 2)
        self.assertEqual(fib(3), 3)
        self.assertEqual(fib(4), 5)


@pytest.fixture
def x():
    return 5
    
@pytest.yield_fixture
def fx():
    yield 8
    

def test_other_fib(x, fx):
    assert fib(x) == fx


def test_known_fibs():
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(4) == 5
    assert fib(5) is not None

