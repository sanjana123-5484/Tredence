

# Mini Workflow Engine — AI Engineering Internship Assignment

This project implements a minimal workflow and graph engine inspired by agent frameworks such as LangGraph. The system allows defining nodes, connecting them through edges, maintaining a shared state, and running workflows through FastAPI APIs. The focus of the implementation is correctness, clarity, and modular backend design.

The project includes:

* A modular FastAPI backend
* A small, extensible graph engine
* A basic tool registry
* One fully implemented workflow (Option A: Code Review Mini-Agent)

---

## Features

### Workflow Graph

* Nodes implemented as async Python functions
* Edges that define execution order
* A shared mutable state passed between nodes
* Looping via cyclic edges
* Branching via node-controlled `"next"` transitions
* Execution logs showing each step in order

### Tool Registry

Nodes can call reusable tools, including:

* `compute_complexity` – calculates a simple code complexity score
* `detect_smells` – detects TODO, print statements, and FIXME comments

### API Endpoints (FastAPI)

| Method | Endpoint                | Description                                             |
| ------ | ----------------------- | ------------------------------------------------------- |
| POST   | `/graph/create`         | Create a workflow graph                                 |
| POST   | `/graph/run`            | Execute a workflow with initial state                   |
| GET    | `/graph/state/{run_id}` | Fetch the state and logs for a run                      |
| GET    | `/example/create`       | Create an example workflow graph (Code Review workflow) |

---

## Implemented Workflow: Option A — Code Review Mini-Agent

This workflow performs the following steps:

1. Extract functions
2. Check complexity
3. Detect basic issues
4. Suggest improvements
5. Loop until `quality_score >= threshold`

This is a rule-based version, as required in the assignment.

### Nodes

| Node      | Purpose                                            |
| --------- | -------------------------------------------------- |
| extract   | Simulates extracting functions from code           |
| analyze   | Computes code complexity and updates quality score |
| detect    | Detects TODO, print statements, and other issues   |
| suggest   | Generates improvement suggestions                  |
| aggregate | Checks loop condition and routes to the next node  |

The workflow loops from `aggregate` back to `analyze` until the threshold condition is satisfied.

---

## Project Structure

```
app/
    main.py
    api/
        graph_routes.py
        example_routes.py
        schemas.py
    engine/
        graph.py
        nodes.py
        registry.py
    storage/
        memory.py
    workflows/
        code_review.py
requirements.txt
README.md
```

This structure keeps the graph engine, API, workflow logic, and storage cleanly separated.

---

## How to Run the Project

1. Create a virtual environment:

```
python -m venv venv
```

Activate it (Windows):

```
venv\Scripts\activate
```

Or on macOS/Linux:

```
source venv/bin/activate
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Start the FastAPI server:

```
uvicorn app.main:app --reload
```

The application will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---

## How to Test the Workflow

### Step 1: Create the Example Workflow Graph

Send a GET request to:

```
/example/create
```

This returns a graph definition and a `graph_id`.

### Step 2: Run the Workflow

Send a POST request to:

```
/graph/run
```

Example request body:

```json
{
  "graph_id": "PASTE_GRAPH_ID_HERE",
  "state": {
    "code": "def foo():\n print('hello')\n # TODO fix",
    "threshold": 80
  }
}
```

You will receive the updated state, execution logs, and a `run_id`.

### Step 3: Retrieve Run State

```
/graph/state/{run_id}
```

---

## What the Engine Supports

* Node execution using async functions
* Shared state transitions
* Graph-defined execution order
* Conditional branching
* Looping until a termination condition is met
* A simple tool registry
* Modular backend structure

---

## What I Would Improve With More Time

* Replace in-memory storage with SQLite or Postgres
* Add WebSocket support for real-time log streaming
* Improve branching support for multi-path flows
* Add background task execution for long-running nodes
* Introduce state validation using Pydantic models
* Add unit tests and continuous integration
* Add richer logging and error handling

---

## Conclusion

This project demonstrates a clear and modular implementation of a workflow/graph engine using FastAPI, async Python, and well-structured execution logic. It satisfies the requirements for demonstrating state transitions, loop execution, node-based workflow design, and clean backend architecture.


