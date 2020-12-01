import unittest
from .maybe.maybe_test import TestJust
from .either.either_test import TestEither


def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestJust())
    test_suite.addTest(TestEither())
    return test_suite


if __name__ == '__main__':
    suite = create_suite()

    runner = unittest.TextTestRunner()
    runner.run(suite)
