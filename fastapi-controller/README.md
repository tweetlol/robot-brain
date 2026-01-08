# FastAPI Direction Controller

This project is a simple FastAPI application that provides a web interface with four buttons to control a Raspberry Pi in different directions: Up, Down, Left, and Right. Each button triggers a corresponding Python script that contains the logic for that direction.

## Project Structure

```
fastapi-direction-controller
├── src
│   ├── main.py                # Entry point of the FastAPI application
│   ├── routes
│   │   └── directions.py      # Defines routes for handling button clicks
│   └── scripts
│       ├── up.py              # Logic for the "Up" direction
│       ├── down.py            # Logic for the "Down" direction
│       ├── left.py            # Logic for the "Left" direction
│       └── right.py           # Logic for the "Right" direction
├── static
│   └── style.css              # CSS styles for the webpage
├── templates
│   └── index.html             # HTML template for the webpage
├── requirements.txt           # Lists project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd fastapi-direction-controller
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the FastAPI application**:
   ```
   uvicorn src.main:app --reload
   ```

5. **Access the web interface**:
   Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

Click on the buttons to execute the corresponding scripts for each direction. The application will handle the requests and trigger the appropriate Python scripts on your Raspberry Pi.

## License

This project is licensed under the MIT License.