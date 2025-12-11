from fastapi import APIRouter
from app.storage.memory import GRAPHS
from app.api.schemas import ExampleGraphResponse
import uuid

router = APIRouter()

@router.get("/example/create", response_model=ExampleGraphResponse)
def create_example_graph():
    graph = {
        "nodes": {
            "extract": {},
            "analyze": {},
            "detect": {},
            "suggest": {},
            "aggregate": {},
        },
        "edges": {
            "extract": "analyze",
            "analyze": "detect",
            "detect": "suggest",
            "suggest": "aggregate",
            "aggregate": "analyze",
        },
        "start_node": "extract",
    }

    graph_id = str(uuid.uuid4())
    GRAPHS[graph_id] = graph
    return {"graph_id": graph_id, "graph": graph}
