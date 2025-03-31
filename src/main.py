from fastapi import FastAPI
from src.api.controllers.module import modules

app = FastAPI()

for router in modules():
    app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)