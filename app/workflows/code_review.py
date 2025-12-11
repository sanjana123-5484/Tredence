from app.engine.nodes import (
    extract_node, analyze_node, detect_node,
    suggest_node, aggregate_node
)
from app.engine.registry import NODE_REGISTRY, TOOLS

def detect_smells(code: str):
    issues = 0
    reasons = []
    if "TODO" in code:
        issues += 1
        reasons.append("TODO found")
    if "print(" in code:
        issues += 1
        reasons.append("print found")
    if "FIXME" in code:
        issues += 1
        reasons.append("FIXME found")
    return {"issues": issues, "reasons": reasons}

def compute_complexity(code: str):
    lines = code.strip().splitlines()
    complexity = len(lines)
    for kw in ["if ", "for ", "while ", "elif ", "else"]:
        complexity += sum(1 for l in lines if kw in l)
    return {"complexplexity": complexity}

def register_code_review_nodes():
    NODE_REGISTRY["extract"] = extract_node
    NODE_REGISTRY["analyze"] = analyze_node
    NODE_REGISTRY["detect"] = detect_node
    NODE_REGISTRY["suggest"] = suggest_node
    NODE_REGISTRY["aggregate"] = aggregate_node

    TOOLS["detect_smells"] = detect_smells
    TOOLS["compute_complexity"] = compute_complexity
