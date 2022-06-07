import DarkFort
import unittest


class TestDarkFort(unittest.TestCase):

    def test_dice(self):
        # self.assertEqual(DarkFort.dice(2,4), 1)
        for _ in range(10):
        #     print(DarkFort.dice(1,4))
            print(DarkFort.dice(4,2))

if __name__ == '__main__':
    unittest.main()