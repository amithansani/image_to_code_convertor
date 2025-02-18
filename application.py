from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import asyncio
from snap_to_code import SnapToCode

app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    with open("index.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.get("/progress.html")
def read_progress():
    with open("progress.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

# ✅ 1️⃣ NEW: Start the process via POST request
@app.post("/generate_code")
async def generate_code_endpoint(request: Request):
    data = await request.json()
    global input_path, output_path
    input_path = Path(data["input_path"])
    output_path = Path(data["output_path"])

    if not input_path.exists() or not output_path.exists():
        return {"error": "One or both folder paths do not exist"}

    return {"message": "Processing started, go to /progress.html to view progress"}

# ✅ 2️⃣ NEW: Stream progress updates using GET request
@app.get("/progress")
async def progress():
    return StreamingResponse(run_code_generation(input_path, output_path), media_type="text/event-stream")


async def run_code_generation(input_path, output_path):
    snap = SnapToCode(input_path, output_path)
    async for update in snap.run():
        yield f"data: {update}\n\n"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
