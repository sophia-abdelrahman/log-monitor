# log-monitor
A RESTful API to fetch and filter logs from /var/log of Unix-based servers on-demand

## Prerequisites
- Python 3.8 or higher
- Pip

## Installation
1. Create a virtual environment (optional)
```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
2. Install the required packages
```
pip install -r requirements.txt
```

## Usage
### Running the application
Development mode
```
make run
```
or
```
FLASK_APP=app FLASK_ENV=development flask run
```
### API Endpoint
To retrieve logs:

`GET /logs`

Query Parameters:

- filename: Name of the log file to retrieve (e.g., example.log).
- keyword (optional): Keyword to filter log lines (e.g., DEBUG).
- last_n (optional): Number of most recent log lines to retrieve. Default is 10.

### UI
Visit http://localhost:5000 in your web browser to access a basic user interface for interacting with the log monitor.

## Testing
To generate log files:
```
make log name=example.log size=0.1
```
Parameters (required):
- name: Name of the log file
- size: Size of the log file in GB

To run unit tests:
```
python -m unittest test_utils.py
python -m unittest test_views.py
```
