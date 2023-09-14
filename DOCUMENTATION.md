Note: This documentation outlines the main functional and testing files of the project, and does not encompass all files in the project

### Design
`app/__init__.py`
- Initializes the Flask app
- Imports routes from `views.py`

`app/views.py`
- Serves as the HTTP server/API for the application
- Imports the Flask app instance from `__init__.py`
- Exposes an endpoint (`/logs`) for RESTful retrieval of log data
- Handles query parameters: `filename`, `keyword`, and `last_n`
- Utilizes functions from `utils.py` for log retrieval and filtering from `/var/log`

`app/utils.py`
- Contains core logic for accessing and filtering log data
- Efficiently reads large log files in chunks
- Key functions include `retrieve_logs` and validation for filename, keyword, and last_n

`app/errors.py`
- Defines custom exceptions for error handling during parameter validation
- Main exceptions: `FileNameError`, `KeywordError`,` LastNError`

`config.py`
- Centralizes application settings.
- Specifies the directory for log files (`LOG_DIR`)

### Testing
`tests/generate_log.py`
- Utility to generate sample log files
- Accepts filename and size (in GB) parameters

`tests/test_utils.py`
- Tests utility functions in `utils.py`
- Covers valid and invalid inputs

`tests/test_views.py`
- Tests API endpoints in `views.py`
- Simulates requests and checks outcomes

### Usage
Refer to README.md for detailed setup and usage instructions.
