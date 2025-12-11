from pydantic import BaseModel
from typing import Dict, Any

class ExampleGraphResponse(BaseModel):
    graph_id: str
    graph: Dict[str, Any]
