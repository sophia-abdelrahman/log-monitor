import unittest
import os
from app.utils import validate_filename, validate_keyword, validate_last_n
from app.errors import FileNameError, KeywordError, LastNError
from config import LOG_FILE_PATH


class TestUtils(unittest.TestCase):

    def test_validate_filename_with_valid_name(self):
        """Test that a valid filename passes validation."""
        try:
            validate_filename(LOG_FILE_PATH)
        except FileNameError:
            self.fail(f"validate_filename() raised FileNameError unexpectedly for {LOG_FILE_PATH}.")

    def test_validate_filename_with_invalid_name(self):
        # Invalid filenames to test
        invalid_filenames = ["..", "filename..txt", "..filename.txt", "a" * 256]

        for invalid_filename in invalid_filenames:
            with self.subTest(filename=invalid_filename):
                # Check if the FileNameError is raised for each invalid filename
                with self.assertRaises(FileNameError):
                    validate_filename(invalid_filename)

    def test_validate_keyword_with_valid_keywords(self):
        """Test that valid keywords pass validation."""
        valid_keywords = ["INFO", "ERROR", "keyword", "a" * 100]

        for valid_keyword in valid_keywords:
            with self.subTest(keyword=valid_keyword):
                try:
                    validate_keyword(valid_keyword)
                except KeywordError:
                    self.fail(f"validate_keyword() raised KeywordError unexpectedly for {valid_keyword}.")

    def test_validate_keyword_with_invalid_keywords(self):
        """Test that invalid keywords raise an exception."""
        invalid_keywords = ["", " ", "a" * 101]

        for invalid_keyword in invalid_keywords:
            with self.subTest(keyword=invalid_keyword):
                with self.assertRaises(KeywordError):
                    validate_keyword(invalid_keyword)

    def test_validate_last_n_with_valid_values(self):
        """Test that valid values for last_n pass validation."""
        valid_values = [1, 100, 1000]

        for valid_value in valid_values:
            with self.subTest(last_n=valid_value):
                try:
                    validate_last_n(valid_value)
                except LastNError:
                    self.fail(f"validate_last_n() raised LastNError unexpectedly for {valid_value}.")

    def test_validate_last_n_with_invalid_values(self):
        """Test that invalid values for last_n raise an exception."""
        invalid_values = [-1, 0, "string", 1.5]

        for invalid_value in invalid_values:
            with self.subTest(last_n=invalid_value):
                with self.assertRaises(LastNError):
                    validate_last_n(invalid_value)


if __name__ == "__main__":
    unittest.main()