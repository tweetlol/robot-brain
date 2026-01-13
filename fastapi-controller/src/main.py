from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
import os
import subprocess
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    logger.info(f"Received request to run script: {script_name}")
    
    # Map script names to their file paths
    script_paths = {
        "script1": "/home/fj/robot-brain/GPIO/blinkGPIOpin.py",
        "script2": "/home/fj/robot-brain/GPIO/fancyGPIOpins.py",
    }
    
    if script_name not in script_paths:
        logger.error(f"Script '{script_name}' not found in mapping")
        raise HTTPException(status_code=404, detail=f"Script '{script_name}' not found")
    
    script_path = script_paths[script_name]
    logger.info(f"Script path: {script_path}")
    
    if not os.path.exists(script_path):
        logger.error(f"Script file does not exist: {script_path}")
        raise HTTPException(status_code=404, detail=f"Script file not found: {script_path}")
    
    try:
        # Run the script and wait for it to complete to capture any errors
        logger.info(f"Starting script: {script_path}")
        result = subprocess.run(
            ["python3", script_path],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(script_path),
            timeout=30  # 30 second timeout
        )
        
        logger.info(f"Script completed with return code: {result.returncode}")
        logger.info(f"STDOUT: {result.stdout}")
        if result.stderr:
            logger.error(f"STDERR: {result.stderr}")
        
        if result.returncode != 0:
            raise HTTPException(
                status_code=500, 
                detail=f"Script failed with error: {result.stderr}"
            )
        
        return {
            "status": "success",
            "message": f"Script '{script_name}' executed successfully",
            "script_path": script_path,
            "output": result.stdout,
            "error": result.stderr if result.stderr else None
        }
    except subprocess.TimeoutExpired:
        logger.error("Script execution timed out")
        raise HTTPException(status_code=500, detail="Script execution timed out after 30 seconds")
    except Exception as e:
        logger.error(f"Failed to run script: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to run script: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
