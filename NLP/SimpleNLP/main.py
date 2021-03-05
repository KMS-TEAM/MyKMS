from simpleNLP import SimpleNLP
from neo4japi import Neo

if __name__ == "__main__":
    print("Hello from NLP")
    scheme = "neo4j"  # Connecting to Aura, use the "neo4j+s" URI scheme
    host_name = "localhost"
    port = 7687
    url = "{scheme}://{host_name}:{port}".format(scheme=scheme, host_name=host_name, port=port)
    user = "neo4j"
    password = "admin"
    app = Neo(url, user, password)
    app.create_friendship("Alice", "David")
    app.find_person("Alice")
    app.close()


