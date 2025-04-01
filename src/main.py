from fastapi import FastAPI
from src.api.controllers.module import routes

app = FastAPI()

for router in routes():
    app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)