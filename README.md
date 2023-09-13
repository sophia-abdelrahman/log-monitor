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
Access a basic user interface for interacting with the log monitor:
```
http://localhost:5000/logs
```
or
```
http://127.0.0.1:5000/logs
```

## Testing
To generate log files:
```
make log name=example.log size=0.1
```
or
```
TODO: Alterative for windows users with generate_log.py
```

To run unit tests:
```
python -m unittest test_utils.py
python -m unittest test_views.py
```

To test with curl:
```
curl "http://localhost:5000/logs?filename=EXAMPLE.log&keyword=ERROR&last_n=10"
```
