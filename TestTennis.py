import unittest
from Tennis import Tennis


class TestTennis(unittest.TestCase):

    def test_uno(self):
        tennis = Tennis()
        tennis.juego()

if __name__ == "__main__":
    unittest.main()
