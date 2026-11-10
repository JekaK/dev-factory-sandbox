# SPDX-License-Identifier: MIT
import unittest

from labels import file_count


class FileCountZeroTest(unittest.TestCase):
    def test_zero_count(self):
        self.assertEqual(file_count(0), "0 files")
