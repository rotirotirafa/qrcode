import unittest
from utils import create_files_directory, remove_files_directory


class DefaultQrCodeTestCase(unittest.TestCase):

    def test_create_files_directory(self):
        self.assertTrue(create_files_directory)

    def test_remove_files_directory(self):
        self.assertTrue(remove_files_directory)
