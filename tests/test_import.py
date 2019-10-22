import unittest

# only test that linuxdoc can be imported
import linuxdoc

class TestNone(unittest.TestCase):
    def test_none(self):
        self.assertEqual(True, True)
