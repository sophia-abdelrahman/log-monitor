import unittest
from app import app
from config import DEFAULT_LAST_N, LOG_FILE_NAME

class TestViews(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_missing_filename(self):
        response = self.client.get('/logs')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid filename. Ensure it's a string between 1-255 characters without '..'.", response.get_data(as_text=True))

    def test_valid_filename_default_parameters(self):
        response = self.client.get('/logs', query_string={'filename': LOG_FILE_NAME})
        self.assertEqual(response.status_code, 200)

    def test_invalid_filename(self):
        response = self.client.get('/logs', query_string={'filename': 'invalid..log'})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Invalid filename", response.data)

    def test_valid_keyword(self):
        response = self.client.get('/logs', query_string={'filename': LOG_FILE_NAME, 'keyword': 'INFO'})
        self.assertEqual(response.status_code, 200)

    def test_invalid_keyword(self):
        response = self.client.get('/logs', query_string={'filename': LOG_FILE_NAME, 'keyword': ' ' * 101})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Invalid keyword", response.data)

    def test_keyword_filtering(self):
        response = self.client.get('/logs', query_string={'filename': LOG_FILE_NAME, 'keyword': 'ERROR'})
        data = response.get_json()
        lines = data['lines']

        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(len(lines), DEFAULT_LAST_N)
        self.assertTrue(all('ERROR' in line for line in lines))

    def test_valid_last_n(self):
        response = self.client.get('/logs', query_string={'filename': LOG_FILE_NAME, 'last_n': '5'})
        self.assertEqual(response.status_code, 200)

    def test_invalid_last_n(self):
        response = self.client.get('/logs', query_string={'filename': LOG_FILE_NAME, 'last_n': '-5'})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"last_n should be a positive integer", response.data)


if __name__ == '__main__':
    unittest.main()


# import unittest
# from app import app
# from config import DEFAULT_LAST_N, LOG_FILE_NAME
# from app.errors import FileNameError, KeywordError, LastNError
#
# class TestViews(unittest.TestCase):
#
#     def setUp(self):
#         app.testing = True
#         self.client = app.test_client()
#
#     def test_missing_filename(self):
#         response = self.client.get('/logs')
#         self.assertEqual(response.status_code, 400)
#         self.assertIn("filename is required", response.get_data(as_text=True))
#
#     def test_valid_filename_default_parameters(self):
#         response = self.client.get('/logs', query_string={'filename': 'LOG_FILE_NAME.log'})
#         self.assertEqual(response.status_code, 200)
#
#     def test_invalid_filename(self):
#         response = self.client.get('/logs', query_string={'filename': 'invalid..log'})
#         self.assertEqual(response.status_code, 400)
#         self.assertIn(b"Invalid filename", response.data)
#
#     def test_valid_keyword(self):
#         response = self.client.get('/logs', query_string={'filename': LOG_FILE_NAME, 'keyword': 'INFO'})
#         self.assertEqual(response.status_code, 200)
#
#     def test_invalid_keyword(self):
#         response = self.client.get('/logs', query_string={'filename': LOG_FILE_NAME, 'keyword': ' ' * 101})
#         self.assertEqual(response.status_code, 400)
#         self.assertIn(b"Invalid keyword", response.data)
#
#     def test_keyword_filtering(self):
#         response = self.app.get('/logs', query_string={'filename': LOG_FILE_NAME, 'keyword': 'ERROR'})
#         data = response.get_json()
#         lines = data['lines']
#
#         # Ensure the response status code is 200 (OK)
#         self.assertEqual(response.status_code, 200)
#
#         # Ensure the number of lines returned is up to DEFAULT_LAST_N and they all contain the keyword 'ERROR'
#         self.assertLessEqual(len(lines), DEFAULT_LAST_N)
#         for line in lines:
#             self.assertIn('ERROR', line)
#
#         # Check if every line in the response contains the keyword 'ERROR'
#         lines = response.json['lines']
#         self.assertTrue(all('ERROR' in line for line in lines))
#
#         # As an example, let's say we expect 5 lines with the keyword 'ERROR' in the log file.
#         self.assertEqual(len(lines), 5)
#
#     def test_valid_last_n(self):
#         response = self.client.get('/logs', query_string={'filename': LOG_FILE_NAME, 'last_n': '5'})
#         self.assertEqual(response.status_code, 200)
#
#     def test_invalid_last_n(self):
#         response = self.client.get('/logs', query_string={'filename': LOG_FILE_NAME, 'last_n': '-5'})
#         self.assertEqual(response.status_code, 400)
#         self.assertIn(b"last_n should be a positive integer", response.data)
#
#
# if __name__ == '__main__':
#     unittest.main()
