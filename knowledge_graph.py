# Node - Name, Edges
class Node:
    def __init__(self,name):
        self.name=name
        self.edges=[]
    def add_edge(self,edge):
        self.edges.append(edge)

# Edges - Source, Target, Relation
class Edge:
    def __init__(self,source,target,relation):
        self.source=source
        self.target=target
        self.relation=relation

# Knowledge Graph - Nodes, Edges, Relationship
class KG:
    def __init__(self,name):
        self.name=name
        self.nodes={}
    def add_node(self, node_name):
        if node_name not in self.nodes:
            self.nodes[node_name] = Node(node_name)
        return self.nodes[node_name]
    def add_edge(self, source_name, target_name, relation):
        source = self.add_node(source_name)
        target = self.add_node(target_name)
        edge = Edge(source, target, relation)
        source.add_edge(edge)
    def display(self):
        for node in self.nodes.values():
            for edge in node.edges:
                print(f"{edge.source.name} -[{edge.relation}]-> {edge.target.name}")


if __name__=="__main__":
    graph=KG("Family Tree")
    graph.add_edge("A", "B", "is father of")
    graph.add_edge("B", "C", "is sibling of")
    graph.add_edge("A", "C", "is father of")
    graph.add_edge("A", "D", "is partner of")
    graph.add_edge("D", "B", "is mother of")
    graph.add_edge("D", "C", "is mother of")
    print("Knowledge Graph:")
    graph.display()

    # To check the knowledge graph is working efficiently or not?
    print("\nQueries:")
    print("Is A father of B?", graph.check_relation("A", "B", "is father of"))
    print("Is B sibling of C?", graph.check_relation("B", "C", "is sibling of"))
    print("Is D mother of A?", graph.check_relation("D", "A", "is mother of"))