import networkx as nx

def build_graph():
    G = nx.DiGraph()

    edges = [
        ('super_source', 'T1', 1000), ('super_source', 'T2', 1000),  # Додаємо "супер-джерело"
        ('T1', 'S1', 25), ('T1', 'S2', 20), ('T1', 'S3', 15),
        ('T2', 'S3', 15), ('T2', 'S4', 30), ('T2', 'S2', 10),
        ('S1', 'M1', 15), ('S1', 'M2', 10), ('S1', 'M3', 20),
        ('S2', 'M4', 15), ('S2', 'M5', 10), ('S2', 'M6', 25),
        ('S3', 'M7', 20), ('S3', 'M8', 15), ('S3', 'M9', 10),
        ('S4', 'M10', 20), ('S4', 'M11', 10), ('S4', 'M12', 15),
        ('S4', 'M13', 5), ('S4', 'M14', 10),
        ('M1', 'super_sink', 1000), ('M2', 'super_sink', 1000),
        ('M3', 'super_sink', 1000), ('M4', 'super_sink', 1000),
        ('M5', 'super_sink', 1000), ('M6', 'super_sink', 1000),
        ('M7', 'super_sink', 1000), ('M8', 'super_sink', 1000),
        ('M9', 'super_sink', 1000), ('M10', 'super_sink', 1000),
        ('M11', 'super_sink', 1000), ('M12', 'super_sink', 1000),
        ('M13', 'super_sink', 1000), ('M14', 'super_sink', 1000)
    ]

    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)

    return G

def compute_max_flow(G):
    flow_value, flow_dict = nx.maximum_flow(G, 'super_source', 'super_sink')
    return flow_value, flow_dict

def main():
    G = build_graph()
    max_flow, flow_dict = compute_max_flow(G)

    print(f"Maximum Flow: {max_flow}")
    print("Flow Distribution:")
    for u, flows in flow_dict.items():
        for v, flow in flows.items():
            if flow > 0:
                print(f"{u} -> {v}: {flow}")

if __name__ == "__main__":
    main()
