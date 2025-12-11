from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from app.storage.memory import GRAPHS, RUNS
from app.engine.graph import execute_graph
from app.engine.registry import TOOLS
from app.engine.registry import NODE_REGISTRY
from app.workflows.code_review import register_code_review_nodes
import uuid

router = APIRouter()

register_code_review_nodes()   


class CreateGraphRequest(BaseModel):
    nodes: Dict[str, Any]
    edges: Dict[str, str]
    start_node: str

class RunGraphRequest(BaseModel):
    graph_id: str
    state: Dict[str, Any]


@router.post("/create")
def create_graph(req: CreateGraphRequest):
    graph_id = str(uuid.uuid4())
    GRAPHS[graph_id] = req.dict()
    return {"graph_id": graph_id}


@router.post("/run")
async def run_graph(req: RunGraphRequest):
    if req.graph_id not in GRAPHS:
        raise HTTPException(404, "Graph not found")

    run_id = str(uuid.uuid4())
    state = req.state

    final_state, logs = await execute_graph(GRAPHS[req.graph_id], state, TOOLS)

    RUNS[run_id] = {"state": final_state, "log": logs}

    return {"run_id": run_id, "final_state": final_state, "log": logs}


@router.get("/state/{run_id}")
def get_state(run_id: str):
    if run_id not in RUNS:
        raise HTTPException(404, "Run not found")
    return RUNS[run_id]
