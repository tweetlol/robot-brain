# FastAPI Controller

A simple FastAPI boilerplate project for controlling a robot on Raspberry Pi via web interface.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Or simply:
```bash
python src/main.py
```

3. Access the webpage:
- Local: `http://localhost:8000`
- LAN: `http://<your-raspberry-pi-ip>:8000`

## Project Structure

```
fastapi-controller/
├── src/
│   └── main.py          # Main FastAPI application
├── templates/           # HTML templates (optional)
├── static/             # Static files (CSS, JS, images)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Notes

- The `--reload` flag enables auto-restart on code changes (development only)
- `--host 0.0.0.0` makes the server accessible from other machines on your network
- For production, remove the `--reload` flag
