# MyKMS

## Neo4j install

sudo apt update

sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -

sudo add-apt-repository "deb https://debian.neo4j.com stable 4.1"

sudo apt install neo4j

sudo systemctl enable neo4j.service

sudo systemctl status neo4j.service

## Add APOC Plugin

### Download .jar

Since APOC relies on Neo4j’s internal APIs you need to use the matching APOC version for your Neo4j installaton. Make sure that the first two version numbers match between Neo4j and APOC.

| apoc | neo4j version |
| :---: | :---: | 
| 4.2.0.1# | 4.2.2(4.2.x) |
| 4.1.0.4  | 4.1.1 (4.1.x) |
| .......  | ........ |

You can find all releases here.

https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/

### Add .jar to /var/lib/neo4j/plugins

### Create apoc.conf in /etc/neo4j/

apoc.import.file.enabled=true
apoc.import.file.use_neo4j_config=true
apoc.trigger.enabled=true
apoc.ttl.enabled=true


### Adjust the neo4j conf file (/etc/neo4j/neo4j.conf)

dbms.security.procedures.unrestricted=apoc.*

### Restart Neo4j

sudo systemctl restart neo4j.service





