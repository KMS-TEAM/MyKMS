# Using simpleNLP => processing text data => entity pairs + relations
# Using neo4japi => create node in neo4j from data got in simplNLP
# Some function to get data from neo4j (delete, find, update, add)
import simpleNLP as xxx
import neo4japi as api
import networkx as nx

class Api_Neo4j():
    def __init__(self, data=None, name=''):

    def create_node(self):
        G = nx.Graph()
        self.single = G.add_node()
        self.MultiGrap = G.add_edges_from()

    def handle_text(self):
        doc = xxx.SimpleNLP(u"data/input/test.txt")
        doc.NLPrun()
        return doc.relations, doc.target, doc.source

    def Cypher(self):