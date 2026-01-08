from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import os
import subprocess

app = FastAPI()

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Setup templates
templates_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
templates = Jinja2Templates(directory=templates_dir)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.post("/api/run/{script_name}")
async def run_script(script_name: str):
    """
    Run a Python script on the Raspberry Pi.
    Update the script paths below to point to your actual scripts.
    """
    # Map script names to their file paths
    script_paths = {
        "script1": "/home/fj/robot-brain/GPIOpin-basics/blinkGPIOpin.py",
        "script2": "/home/fj/robot-brain/GPIOpin-basics/fancyGPIOpins.py",
    }
    
    if script_name not in script_paths:
        raise HTTPException(status_code=404, detail=f"Script '{script_name}' not found")
    
    script_path = script_paths[script_name]
    
    if not os.path.exists(script_path):
        raise HTTPException(status_code=404, detail=f"Script file not found: {script_path}")
    
    try:
        # Run the script in the background
        # Use subprocess.Popen for non-blocking execution
        process = subprocess.Popen(
            ["python3", script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        return {
            "status": "success",
            "message": f"Script '{script_name}' started successfully",
            "script_path": script_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to run script: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
