import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "First test for run"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

