from neo4j import GraphDatabase

driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "1"))

def add_friend(tx, name, lable, location, phonenumber):
    tx.run("CREATE (a:Person {name: $name})", name=name)
    return None
def print_friends(tx, name):
    result = tx.run("MATCH (a:Person {name: $name})", name=name)
    return result.single()
def update_friends(tx, live, name):
    tx.run ("MATCH (a:Person {name: $name})"
            "SET a.live = $live", live=live, name = name)
    return None
with driver.session() as session:
#    session.write_transaction(add_friend, "Arthur")
    session.write_transaction(update_friends, "HongKong", "Arthur")
    session.read_transaction(print_friends, "Arthur")
driver.close()
