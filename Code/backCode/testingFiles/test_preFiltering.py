import ..preFiltering
from Code.backCode.preFiltering import *
import unittest
import os

class TestpreFiltering(unittest.TestCase):

    def test_createDirectory(self):
        result = preFiltering.createDirectory(topPath + "\\" + "files", 'filesRenamed')
        self.assertEqual(result, os.getcwd() + "\\" + "files", 'filesRenamed')

    def test_getFiles(self):
        pass

if __name__ == "__main__":
    unittest.main()