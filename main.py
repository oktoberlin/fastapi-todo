from fastapi import FastAPI
import uvicorn
from core.urls import router_configs

app = FastAPI()

for router, prefix, tags in router_configs:
    app.include_router(router, prefix=prefix, tags=tags)

@app.get("/")
async def root():
    return {"Hello": "World!"}


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)