from fastapi import FastAPI
from routes.students import students_router
from routes.staff import staff_router
from routes.teachers import teachers_router
from routes.marketing import marketing_router
from routes.commercial import commercial_router
from routes.metrics import metrics_router

app = FastAPI()
app.include_router(students_router)
app.include_router(teachers_router)  # Register specific routes first
app.include_router(marketing_router)
app.include_router(commercial_router)
app.include_router(staff_router)  # Register parameterized routes after
app.include_router(metrics_router)

@app.get("/", tags=["test"])
async def root():
    return {"message": "Hello World"}
