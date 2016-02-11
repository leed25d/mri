import unittest
import os
import stat
from ..slice_reader import SliceReader


class SliceReaderTest(unittest.TestCase):
    def test_0001(self):
        '''
        Make sure that the slice reader can be instantiated
        '''
        self.assertIsNotNone(SliceReader())
        self.assertIsNotNone(SliceReader('test_data/good_data_001.in'))

    def test_0010(self):
        '''
        Make sure that the slice reader can read a known good file with capital and small letters
        '''
        path = 'mri_lib/tests/data_files'
        test_result = """aaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaa
aaaaabbbbbbaaaaaaaaa
aaaaabbbbbbaaaaaaaaa
aaaaabbbbbbaaaaaaaaa
aaaaabbbbbbaacccccaa
aaaaaaaaaaaaacccccaa
aaaaaaaaaaaaacccccaa
aaaaaaaaaaaaaaaaaaaa
"""
        s = SliceReader(path + '/good_data_001.in')
        s.read_file()
        self.assertEqual(test_result, s.in_xlated)

    def test_0020(self):
        '''
        Make sure that the slice reader can read a known good file with capital and small letters and extra ignored characters
        '''
        path = 'mri_lib/tests/data_files'
        test_result = """aaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaa
aaaaabbbbbbaaaaaaaaa
aaaaabbbbbbaaaaaaaaa
aaaaabbbbbbaaaaaaaaa
aaaaabbbbbbaacccccaa
aaaaaaaaaaaaacccccaa
aaaaaaaaaaaaacccccaa
aaaaaaaaaaaaaaaaaaaa
"""
        s = SliceReader(path + '/good_data_005.in')
        s.read_file()
        self.assertEqual(test_result, s.in_xlated)

    def test_0030(self):
        '''
        Make sure that the slice reader throws an error for an unreadable file
        '''
        f_path = 'mri_lib/tests/data_files/good_data_010.in'
        os.chmod(f_path, 0)
        s = SliceReader(f_path)
        with self.assertRaises(ValueError):
            s.read_file()
        os.chmod(f_path, stat.S_IRUSR + stat.S_IRGRP + stat.S_IROTH)

    def test_0040(self):
        '''
        Make sure that the slice reader throws an error for a malformed file
        '''
        f_path = 'mri_lib/tests/data_files/bad_data_empty_row.in'
        s = SliceReader(f_path)
        with self.assertRaises(ValueError):
            s.read_file()
