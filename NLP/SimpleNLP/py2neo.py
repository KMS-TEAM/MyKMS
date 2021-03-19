from py2neo.data import Node, Relationship
driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "1"))
            a = Node("Person", name="Alice")
            b = Node("Person", name="Bob")
            ab = Relationship(a, "KNOWS", b)
            ab