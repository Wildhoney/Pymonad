import unittest
from Maybe import Maybe


a = Maybe('Adam')
b = Maybe(None)


def lower(x): return x.lower()
def reverse(x): return x[::-1]
def shout(x): return '%s!' % x
def capitalise(x): return x.capitalize()


class TestMaybe(unittest.TestCase):

    def test_is_none(self):
        self.assertEqual(a.is_none(), False)
        self.assertEqual(b.is_none(), True)

    def test_is_just(self):
        self.assertEqual(a.is_just(), True)
        self.assertEqual(b.is_just(), False)

    def test_map(self):
        x = a.map(lower).map(reverse).map(shout).map(capitalise)
        self.assertEqual(str(x), "Just (Mada!)")

    def test_map_shorthand(self):
        x = a >> lower >> reverse >> shout >> capitalise
        self.assertEqual(str(x), "Just (Mada!)")

    def test_get(self):
        x = a >> lower >> reverse >> shout >> capitalise
        y = b >> lower >> reverse >> shout >> capitalise

        self.assertEqual(x.get(), "Mada!")
        self.assertEqual(y.get("Unknown"), "Unknown")

    def test_get_shorthand(self):
        x = a >> lower >> reverse >> shout >> capitalise
        y = b >> lower >> reverse >> shout >> capitalise

        self.assertEqual(x | "Unknown", "Mada!")
        self.assertEqual(y | "Unknown", "Unknown")


if __name__ == '__main__':
    unittest.main()
