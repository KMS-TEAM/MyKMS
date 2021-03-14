from neo4j import GraphDatabase
import simpleNLP as xxx
import networkx as nx
driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "1"))

def creat_source(tx , title ):
     tx.run("CREATE (source:entitiy_1{title: $title})", title=title )
     return None
def creat_target(tx, title):
     tx.run ("CREATE (target:entitiy_1{title: $title})", title=title)
def creat_relation (tx, relation, title, source):
     query = (
        "CREATE (p1:Person { name: $title }) "
        "CREATE (p2:Person { name: $source }) "
        "CREATE p = (p1)-[:relation {infor: $relation}]->(p2) "
        "RETURN p"
    )
     tx.run(query, title=title,source=source, relation=relation )
     return None
def print_friends(tx, name):
    result = tx.run("MATCH (a:Person {name: $name})", name=name)
    return result.single()
def update_friends(tx, live, name):
    tx.run ("MATCH (a:Person {name: $name})"
            "SET a.live = $live", live=live, name = name)
    return None

#    session.write_transaction(update_friends, "HongKong", "Arthur")
#    session.read_transaction(print_friends, "Arthur")
driver.close()
if __name__ == "__main__":
    test = xxx.SimpleNLP(u"data/input/test.txt")
    test.NLPrun()
    relations = test.relations
    sources = test.source
    targets = test.target
    kg = test.kg_df
    Graph= test.G
    #pos = nx.spring_layout(Graph)
    #nx.draw(Graph, with_labels=True, node_color='skyblue', pos=pos)
    #with driver.session() as session:
            #for source in test.source():
            #     session.write_transaction(creat_source, source)
            #for target in test.target():
            #    session.write_transaction(creat_target, target)
            #for relation in test.get_relation():
            #    session.write_transaction(creat_relation,relation.get_relation, relation.target, relation.source)

            #print(test.number())
            #for i in range(1, test.numbers()):
            #    relation = relations[i]
            #    source = sources[i]
            #    target = targets[i]
            #    print(source, '!', relation, '!', target)
            #    session.write_transaction(creat_relation, relation, target, source)

