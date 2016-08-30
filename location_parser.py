import os
from bs4 import BeautifulSoup as Soup
from neo4j.v1 import GraphDatabase, basic_auth

# You may customize your DB location and password here
NEO4J_DB_PATH = os.environ.get('NEO4J_DB_PATH ', 'bolt://localhost')
NEO4J_DB_USER = os.environ.get('NEO4J_DB_USER ', 'neo4j')
NEO4J_DB_PW = os.environ.get('NEO4J_DB_PW', 'neo4j')


def init_nodes_from_xml(filename):
    """Init the locaitons(county, such as New Taipei City),
    and location(city or township, such as Panchaio) as node into neo4j
    """
    with open(filename, 'r') as file:
        soup = Soup(file.read(), 'lxml')

        locations = soup.find_all('locations')[0]
        print(locations.locationsname.string.strip(), os.path.split(filename)[-1])
        location_set = soup.find_all('location')
        for location in location_set:
            print(location.geocode.string.strip(), location.locationname.string.strip())
    # driver = GraphDatabase.driver(NEO4J_DB_PATH, auth=basic_auth(NEO4J_DB_USER, NEO4J_DB_PW))
    # session = driver.session()

    # session.run("CREATE (a:Person {name:'Arthur', title:'King'})")
    #
    # result = session.run("MATCH (a:Person) WHERE a.name = 'Arthur' RETURN a.name AS name, a.title AS title")
    # for record in result:
    #     print("%s %s" % (record["title"], record["name"]))

    # session.close()
    print(filename)


if __name__ == '__main__':
    init_nodes_from_xml('/home/yanganto/KlesanWatcher/data/F-D0047-001')

