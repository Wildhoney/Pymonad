import unittest
from .right import Right
from .left import Left


a = Right('Adam')
b = Left("Name cannot be retrieved")


def lower(x): return x.lower()
def reverse(x): return x[::-1]
def shout(x): return '%s!' % x
def capitalise(x): return x.capitalize()


class TestEither(unittest.TestCase):

    def test_is_right(self):
        self.assertEqual(a.is_right(), True)
        self.assertEqual(b.is_right(), False)

    def test_is_left(self):
        self.assertEqual(a.is_left(), False)
        self.assertEqual(b.is_left(), True)

    def test_map(self):
        c = a.map(lower).map(reverse).map(shout).map(capitalise)
        self.assertEqual(str(c), "Right (Mada!)")
        d = a.map(lower).map(lambda x: Right(reverse(x))).map(shout).map(capitalise)
        self.assertEqual(str(d), "Right (Mada!)")

        e = b.map(lower).map(reverse).map(shout).map(capitalise)
        self.assertEqual(str(e), "Left (Name cannot be retrieved)")
        f = b.map(lower).map(lambda x: Just(reverse(x))).map(shout).map(capitalise)
        self.assertEqual(str(f), "Left (Name cannot be retrieved)")


    def test_map_shorthand(self):
        c = a >> lower >> reverse >> shout >> capitalise
        self.assertEqual(str(c), "Right (Mada!)")
        d = b >> lower >> reverse >> shout >> capitalise
        self.assertEqual(str(d), "Left (Name cannot be retrieved)")

    def test_get(self):
        c = a >> lower >> reverse >> shout >> capitalise
        self.assertEqual(c.get(), ("Mada!", None))
        d = b >> lower >> reverse >> shout >> capitalise
        self.assertEqual(d.get("Unknown"), ("Unknown", "Name cannot be retrieved"))

    def test_get_shorthand(self):
        c = a >> lower >> reverse >> shout >> capitalise
        self.assertEqual(c | "Unknown", ("Mada!", None))
        d = b >> lower >> reverse >> shout >> capitalise
        self.assertEqual(d | "Unknown", ("Unknown", "Name cannot be retrieved"))
