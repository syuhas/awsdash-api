from fastapi import FastAPI
from api.s3 import router as s3_router




app = FastAPI(root_path='/api')

# test route

@app.get("/health")
async def health():
    return {"status": "I am healthy!"}

app.include_router(s3_router, prefix="/s3", tags=["s3"])

