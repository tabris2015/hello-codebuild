import os
from fastapi import FastAPI
from mangum import Mangum

stage = os.environ.get("STAGE", "local")

app = FastAPI(
    title=f"Awesome API [{stage}]",
    root_path=None if stage == "local" else f"/{stage}"
    )


@app.get("/")
def root():
    return {"message": "hello", "stage": stage}


handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
