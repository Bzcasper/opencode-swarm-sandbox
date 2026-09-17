import unittest
import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertIsNotNone(main)

if __name__ == '__main__':
    unittest.main()
