from app.engine.registry import NODE_REGISTRY

async def execute_graph(graph, state, tools):
    log = []
    node = graph["start_node"]

    for _ in range(50):  
        if node is None:
            break

        fn = NODE_REGISTRY[node]
        result = await fn(state, tools)

        log.append(f"{node}: {result.get('log','')}")

        if result.get("next") is not None:
            node = result["next"]
        else:
            node = graph["edges"].get(node)

    return state, log
