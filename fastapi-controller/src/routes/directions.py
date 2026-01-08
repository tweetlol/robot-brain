from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.get("/A")
async def run_script_A():
    subprocess.run(["python3", "src/scripts/alternateGPIOpins.py"])
    return {"message": "Running script A"}

@router.get("/B")
async def run_script_B():
    subprocess.run(["python3", "src/scripts/fancyGPIOpins.py"])
    return {"message": "Runinng script B"}

@router.get("/C")
async def move_left():
    subprocess.run(["python3", "src/scripts/left.py"])
    return {"message": "Moving left"}

@router.get("/D")
async def move_right():
    subprocess.run(["python3", "src/scripts/right.py"])
    return {"message": "Moving right"}