import os
import uvicorn
from fastapi import FastAPI
from routes.students import students_router
from routes.staff import staff_router
from routes.teachers import teachers_router
from routes.marketing import marketing_router
from routes.commercial import commercial_router
from routes.metrics import metrics_router
from config.auth import login_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://prueba-genuine.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students_router)
app.include_router(teachers_router)  # Register specific routes first
app.include_router(marketing_router)
app.include_router(commercial_router)
app.include_router(staff_router)  # Register parameterized routes after
app.include_router(metrics_router)
app.include_router(login_router)

@app.get("/", tags=["test"])
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

