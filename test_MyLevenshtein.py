import unittest
import MyLevenshtein


class TestLevenshtein(unittest.TestCase):
    def test_substitution(self):

        self.assertEqual(MyLevenshtein.substitution("chien", "chine"), 2)
        self.assertEqual(MyLevenshtein.substitution("cadeau", "radeau"), 1)
        self.assertEqual(MyLevenshtein.substitution("chien", "chien"), 0)

    def test_insertion(self):

        self.assertEqual(MyLevenshtein.insertion("chie", "chien"), 1)
        self.assertEqual(MyLevenshtein.insertion("adeau", "radeau"), 1)
        self.assertEqual(MyLevenshtein.insertion("chien", "chien"), 0)


if __name__ == "__main__":
    unittest.main()
