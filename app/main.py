from fastapi import FastAPI
from app.api.graph_routes import router as graph_router
from app.api.example_routes import router as example_router

app = FastAPI(title="Mini Workflow Engine")

app.include_router(graph_router, prefix="/graph")
app.include_router(example_router)
