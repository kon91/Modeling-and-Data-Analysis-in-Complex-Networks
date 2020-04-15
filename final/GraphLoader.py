import json
from networkx.readwrite import json_graph

subgraph_filename = '/home/tim/Documents/Modeling-and-Data-Analysis-in-Complex-Networks/final/data/' \
                    'subgraph_latest.json'
traffic_graph_filename = '/home/tim/Documents/Modeling-and-Data-Analysis-in-Complex-Networks/final/data/' \
                         'traffic_graph_latest.json'
pages_graph_filename = '/home/tim/Documents/Modeling-and-Data-Analysis-in-Complex-Networks/final/data' \
                       '/hyperlink_graph_builder_output_graph.json'


def load_graph(filename):
    with open(filename) as f:
        js_graph = json.load(f)
    return json_graph.node_link_graph(js_graph)


def load_page_subgraph():
    return load_graph(subgraph_filename)


def load_traffic_graph():
    return load_graph(traffic_graph_filename)


def load_page_graph():
    return load_graph(pages_graph_filename)


def filenames():
    return [subgraph_filename, traffic_graph_filename, pages_graph_filename]