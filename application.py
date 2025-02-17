from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pathlib import Path
import uvicorn
from snap_to_code import SnapToCode

app = FastAPI(title="Snap to Code Converter", description="Converts images to Python code", version="0.0.1")

@app.get("/")
def read_root():
    with open("index.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.post("/generate_code")
async def generate_code_endpoint(request: Request):
    data = await request.json()
    input_path = Path(data["input_path"])
    output_path = Path(data["output_path"])

    if not input_path.exists() or not output_path.exists():
        return {"error": "One or both folder paths do not exist"}

    output = SnapToCode(input_path, output_path).run()
    return {"output": output}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
