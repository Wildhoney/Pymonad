import unittest
from Either import Either


a = Either('Imogen')
b = Either(Exception("Uh-oh!"))


def lower(x): return x.lower()
def reverse(x): return x[::-1]
def shout(x): return '%s!' % x
def capitalise(x): return x.capitalize()
def throw(): raise Exception("Uh-oh!")


class TestEither(unittest.TestCase):

    # def test_is_left(self):
    #     self.assertEqual(a.is_left(), False)
    #     self.assertEqual(b.is_left(), True)

    # def test_is_just(self):
    #     self.assertEqual(a.is_right(), True)
    #     self.assertEqual(b.is_right(), False)

    # def test_map(self):
    #     x = a.map(lower).map(reverse).map(shout).map(capitalise)
    #     self.assertEqual(str(x), "Right (Negomi!)")

    def test_map_shorthand(self):
        x = a >> lower >> reverse >> shout >> capitalise
        y = a >> reverse >> throw >> capitalise
        self.assertEqual(str(x), "Right (Negomi!)")

        print(y)

        # self.assertEqual(str(x), "Left (Negomi!)")

    # def test_get(self):
    #     x = a >> lower >> reverse >> shout >> capitalise
    #     y = b >> lower >> reverse >> shout >> capitalise
    #     z = a >> lower >> reverse >> throw >> shout >> capitalise

    #     # self.assertEqual(x.get(), "Negomi!")
    #     # self.assertEqual(y.get("Unknown"), "Unknown")
    #     print(z)
    #     # self.assertEqual(z.get("Unknown"), "Unknown")

    # def test_get_shorthand(self):
    #     x = a >> lower >> reverse >> shout >> capitalise
    #     y = b >> lower >> reverse >> shout >> capitalise

    #     self.assertEqual(x | "Unknown", "Negomi!")
    #     self.assertEqual(y | "Unknown", "Unknown")

    # def test_get_lambda(self):
    #     self.assertEqual(x | "Unknown", "Negomi!")
    #     self.assertEqual(y | "Unknown", "Unknown")


if __name__ == '__main__':
    unittest.main()
