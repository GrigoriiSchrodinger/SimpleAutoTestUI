import unittest

if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('src/tests')
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
