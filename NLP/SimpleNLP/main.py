from simpleNLP import SimpleNLP
import logging
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
if __name__ == "__main__":
    node = []
    test = SimpleNLP(u"data/input/test.txt")
    data = test.read_txt()
#    print(len(data))
#    nlp = test.word(data[1])
    data = test.get_entitiy_pairs()
    for nlp in data:
        node.append(nlp)
    print (node)
    connect = GraphDatabase.driver(uri="neo4j://localhost:7687", auth=("neo4j", "1"))
    ses = connect.session()
    person_name = "Johan"
    something = "surfing"
    person = "Emil"
    local = "Sweden"
    q1= (
            "MATCH(js:Person) - [:KNOWS]-() - [: KNOWS]-(surfer)"
            "WHERE js.name = $person_name AND surfer.hobby = $something "
            "RETURN DISTINCT surfer"
    )
    q2 = (
        "CREATE(ee:Person {name: $person, from: $local, klout: 99})"
    )

    ses.run(q1, person_name=person_name, something=something)
    ses.run(q2, person=person, local=local)

#   for n in nlp:
#      print(n.text + " " + n.tagging)



