import unittest
import main

class TestMain(unittest.TestCase):
    def test_import(self):
        self.assertIsNotNone(main)

    def test_main_callable(self):
        self.assertTrue(hasattr(main, 'main'))
        self.assertTrue(callable(main.main))

    def test_version_string(self):
        self.assertTrue(hasattr(main, '__version__'))
        self.assertIsInstance(main.__version__, str)

if __name__ == '__main__':
    unittest.main()
