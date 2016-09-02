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
        region, code = locations.locationsname.string.strip(), os.path.split(filename)[-1]
        location_set = soup.find_all('location')
        driver = GraphDatabase.driver(NEO4J_DB_PATH, auth=basic_auth(NEO4J_DB_USER, NEO4J_DB_PW))
        session = driver.session()
        session.run("CREATE (:Region {name:'" + region + "', code:'" + code + "'})")
        for location in location_set:
            geocode, town = location.geocode.string.strip(), location.locationname.string.strip()
            session.run("MATCH (a:Region {name:'" + region + "', code:'" + code + "'}) "
                        "CREATE (a) -[:belong]-> (:town {name:'" + town + "', geocode:'" + geocode + "'})"
                        )
        session.close()

if __name__ == '__main__':
    for dir_path, dir_names, files in os.walk(os.path.join(os.curdir, 'data')):
        for file in files:
            init_nodes_from_xml(os.path.join(dir_path, file))

