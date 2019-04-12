import unittest

from random_repo import get_float
from random_repo import say_something


class TestStuff(unittest.TestCase):

    def test_say_something(self):
        say_something()

    def test_get_float(self):
        retval = get_float()
        print('Got:', retval)
        self.assertIsInstance(retval, float)


if __name__ == '__main__':
    unittest.main()
