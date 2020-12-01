import unittest
from .just import Just
from .nothing import Nothing


a = Just('Adam')
b = Nothing()


def lower(x): return x.lower()
def reverse(x): return x[::-1]
def shout(x): return '%s!' % x
def capitalise(x): return x.capitalize()


class TestJust(unittest.TestCase):

    def test_is_just(self):
        self.assertEqual(a.is_just(), True)
        self.assertEqual(b.is_just(), False)

    def test_is_nothing(self):
        self.assertEqual(a.is_nothing(), False)
        self.assertEqual(b.is_nothing(), True)

    def test_map(self):
        c = a.map(lower).map(reverse).map(shout).map(capitalise)
        self.assertEqual(str(c), "Just (Mada!)")
        d = a.map(lower).map(lambda x: Just(reverse(x))).map(shout).map(capitalise)
        self.assertEqual(str(d), "Just (Mada!)")

        e = b.map(lower).map(reverse).map(shout).map(capitalise)
        self.assertEqual(str(e), "Nothing")
        f = b.map(lower).map(lambda x: Just(reverse(x))).map(shout).map(capitalise)
        self.assertEqual(str(f), "Nothing")


    def test_map_shorthand(self):
        c = a >> lower >> reverse >> shout >> capitalise
        self.assertEqual(str(c), "Just (Mada!)")
        d = b >> lower >> reverse >> shout >> capitalise
        self.assertEqual(str(d), "Nothing")

    def test_get(self):
        c = a >> lower >> reverse >> shout >> capitalise
        self.assertEqual(c.get(), "Mada!")
        d = b >> lower >> reverse >> shout >> capitalise
        self.assertEqual(d.get("Unknown"), "Unknown")

    def test_get_shorthand(self):
        c = a >> lower >> reverse >> shout >> capitalise
        self.assertEqual(c | "Unknown", "Mada!")
        d = b >> lower >> reverse >> shout >> capitalise
        self.assertEqual(d | "Unknown", "Unknown")

