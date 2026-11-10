# SPDX-License-Identifier: MIT
import unittest

from labels import file_count


class FileCountTest(unittest.TestCase):
    def test_positive_counts(self):
        self.assertEqual(file_count(1), "1 file")
        self.assertEqual(file_count(2), "2 files")
