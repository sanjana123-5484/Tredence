import asyncio

async def extract_node(state, tools):
    code = state["code"]
    state["functions"] = [code]
    return {"log": "Extracted functions"}

async def analyze_node(state, tools):
    func = state["functions"][0]
    comp = tools["compute_complexity"](func)

    state["complexity"] = comp["complexplexity"]
    state["quality_score"] = max(0, 100 - comp["complexplexity"])

    return {"log": f"Complexity={state['complexity']} score={state['quality_score']}"}

async def detect_node(state, tools):
    smells = tools["detect_smells"](state["code"])
    state["issues"] = smells["issues"]

    state["quality_score"] -= smells["issues"] * 5
    state["quality_score"] = max(0, state["quality_score"])

    return {"log": f"Issues={state['issues']}"}

async def suggest_node(state, tools):
    suggestions = []

    if state.get("issues", 0) > 0:
        suggestions.append("Clean TODO, FIXME, print statements.")
    if state.get("complexity", 0) > 10:
        suggestions.append("Refactor to reduce complexity.")

    state["suggestions"] = suggestions
    return {"log": "Generated suggestions"}

async def aggregate_node(state, tools):
    threshold = state.get("threshold", 80)
    if state["quality_score"] >= threshold:
        return {"log": "Threshold met — stopping", "next": None}
    return {"log": "Threshold NOT met — looping", "next": "analyze"}
