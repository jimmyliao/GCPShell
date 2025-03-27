from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Define the directory for static files
static_dir = Path(__file__).parent / "static"
static_dir.mkdir(parents=True, exist_ok=True)

# Create a simple index.html file if it doesn't exist
index_html_path = static_dir / "index.html"
if not index_html_path.exists():
    with open(index_html_path, "w") as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>FastAPI Home</title>
</head>
<body>
    <h1>Welcome to the FastAPI Application</h1>
    <p>Go to <a href="/hello">/hello</a> to see the hello endpoint.</p>
</body>
</html>
""")

# Serve static files from the 'static' directory at the root path '/'
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

@app.get("/hello")
async def read_hello():
    return {"message": "Hello from FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
