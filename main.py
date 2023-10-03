from fastapi import FastAPI
from core.urls import router_configs

app = FastAPI()

for router, prefix, tags in router_configs:
    app.include_router(router, prefix=prefix, tags=tags)

@app.get("/")
async def root():
    return {"Hello": "World!"}


