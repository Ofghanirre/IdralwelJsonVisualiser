import pydot

from StepParser import *

node_color = "lightblue"
response_color = "lightgreen"
condition_color = "orange"

def graph_response(graph, responsesList, source):
    for response in responsesList:
        graph.add_node(
            pydot.Node(translate_name(f"{source}_{id(response)}"), shape="hexagon", label=response['id']))
        graph.add_edge(pydot.Edge(translate_name(source),
                                  translate_name(f"{source}_{id(response)}"),
                       label=response["value"], labelangle=0, labeldistance=0.5, decorate=True, fontcolor="purple"))
        graph_response(graph, response["responses"], f"{source}_{id(response)}")

        for link in response["linkStart"]:
            graph.add_edge(pydot.Edge(translate_name(f"{source}_{id(response)}"),
                                      translate_name(link),
                                      color="blue"))

        for link in response["linkStop"]:
            graph.add_edge(pydot.Edge(translate_name(f"{source}_{id(response)}"),
                                      translate_name(link),
                                      arrowhead="dot",
                                      style="dashed",
                                      color="red"))


def create_step_graph(stepParser: StepParser, outputName, output_path = "./output/", pdf=True, png=True, dot=True):
    graph = pydot.Dot(graph_name=outputName, graph_type='digraph', beautify=True, forcelabels=False, rankdir="LR")
    graph.set_node_defaults(nodesep=200.0)

    steps = stepParser.step_list
    for step in steps:
        graph.add_node(pydot.Node(translate_name(step["id"]), shape="box", style="filled", fillcolor=node_color))
        graph.add_node(pydot.Node(translate_name(f"{step['id']}_conditions"), shape="diamond", label="conditions",
                                  style="filled", fillcolor=condition_color))
        graph.add_edge(pydot.Edge(translate_name(step["id"]),
                                  translate_name(f"{step['id']}_conditions")))

        graph.add_node(pydot.Node(translate_name(f"{step['id']}_responses"), shape="diamond", label="responses",
                                  style="filled", fillcolor=response_color))
        graph.add_edge(pydot.Edge(translate_name(step["id"]),
                                  translate_name(f"{step['id']}_responses")))

        for condition in step["conditions"]:
            graph.add_node(pydot.Node(translate_name(f"{step['id']}_{id(condition)}"), shape="hexagon", label=condition))
            graph.add_edge(pydot.Edge(translate_name(f"{step['id']}_conditions"),
                                      translate_name(f"{step['id']}_{id(condition)}")))

        graph_response(graph, step["responses"], f"{step['id']}_responses")

    if (dot):
        graph.write_dot(f"{output_path}{outputName}.dot")
        print(f"|\t Format dot generated as {output_path}{outputName}.dot")
    if (png):
        graph.write_png(f"{output_path}{outputName}.png")
        print(f"|\t Format png generated as {output_path}{outputName}.png")
    if (pdf):
        graph.write_pdf(f"{output_path}{outputName}.pdf")
        print(f"|\t Format pdf generated as {output_path}{outputName}.pdf")

