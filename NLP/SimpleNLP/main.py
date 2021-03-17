from neo4j import GraphDatabase
import simpleNLP as xxx
import networkx as nx

driver = GraphDatabase.driver(uri="neo4j://localhost:7687", auth=('neo4j', '1'))
def creat_source(tx , title ):
     tx.run("CREATE (source:entitiy_1{title: $title})", title=title )
     return
def creat_target(tx, title):
     tx.run ("CREATE (target:entitiy_1{title: $title})", title=title)
def creat_relation (tx, relation, title, source):
     query = (
        "CREATE (p1:Person { name: $title }) "
        "CREATE (p2:Person { name: $source }) "
        "CREATE (p1)-[:relation {infor: $relation}]->(p2) "
        "RETURN p1, p2"
    )
     result = tx.run(query, title=title,source=source, relation=relation )
     return [{"p1": record["p1"]["name"], "p2": record["p2"]["name"]}
             for record in result]

def print_friends(tx, name):
    result = tx.run("MATCH (a:Person {name: $name})", name=name)
    return result.single()
def update_friends(tx, live, name):
    tx.run ("MATCH (a:Person {name: $name})"
            "SET a.live = $live", live=live, name = name)
    return None

#    session.write_transaction(update_friends, "HongKong", "Arthur")
#    session.read_transaction(print_friends, "Arthur")

if __name__ == "__main__":
    with driver.session() as session:
     test = xxx.SimpleNLP(u"data/input/test.txt")
    test.NLPrun()
    relations = test.relations
    sources = test.source
    targets = test.target
    G =[]
    with driver.session() as sesstion:
        for i in range(1, test.numbers()):
            relation = relations[i]
            source = sources[i]
            target = targets[i]
            temp = session.write_transaction(creat_relation, relation, target, source)
            print(temp)

    #nx.write_graphml(G, '/home/nguyen/Documents/database/neo4j/test.graphml')


