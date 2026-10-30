"""反欺诈：用图的连通分量找可疑团伙（对应课件“图计算的基本工具箱”）。

运行：python fraud_ring_graph_components.py
"""
import networkx as nx

MIN_RING_SIZE = 3


def find_suspicious_rings(edges, min_size=MIN_RING_SIZE):
    """返回规模不小于 min_size 的连通分量，每个分量视为一个可疑团伙。"""
    G = nx.Graph()
    G.add_edges_from(edges)
    return [comp for comp in nx.connected_components(G) if len(comp) >= min_size]


def main():
    # 设备A 被三个账户共用
    edges = [("设备A", "账户1"), ("设备A", "账户2"), ("设备A", "账户3")]
    for ring in find_suspicious_rings(edges):
        print("可疑团伙:", ring)


if __name__ == "__main__":
    main()
