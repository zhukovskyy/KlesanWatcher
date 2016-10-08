import os
import urllib.request
import logging

from bs4 import BeautifulSoup as Soup
from neo4j.v1 import GraphDatabase, basic_auth

# You may customize your DB location and password here, else raise LackKeyError
NEO4J_DB_PATH = os.environ.get('NEO4J_DB_PATH ', 'bolt://localhost')
NEO4J_DB_USER = os.environ.get('NEO4J_DB_USER ', 'neo4j')
NEO4J_DB_PW = os.environ.get('NEO4J_DB_PW', 'neo4j')
APP_KEY = os.environ.get('CWB_API', None)


class LackKeyError(PermissionError):
    """Lack of the Key for connection, please set up in environment"""


def init_nodes_from_xml(filename):
    """Init the locaitons(county, such as New Taipei City),
    and location(city or township, such as Panchaio) as node into neo4j
    """
    logging.info('Init data from {}'.format(filename))
    with open(filename, 'r') as file:
        soup = Soup(file.read(), 'lxml')
        locations = soup.find_all('locations')[0]
        region, data_id = locations.locationsname.string.strip(), os.path.split(filename)[-1]
        location_set = soup.find_all('location')
        driver = GraphDatabase.driver(NEO4J_DB_PATH, auth=basic_auth(NEO4J_DB_USER, NEO4J_DB_PW))
        session = driver.session()
        session.run("MERGE (:Region {name:'" + region + "', data_id:'" + data_id + "'})")
        for location in location_set:
            geocode, town = location.geocode.string.strip(), location.locationname.string.strip()
            session.run("MATCH (r:Region {data_id:'" + data_id + "'}) "
                        "MERGE (r) -[:belong]-> (:Town {name:'" + town + "', geocode:'" + geocode + "'})"
                        )
        session.close()


def update_weather_from_data_id(data_id):
    """Update the weather from CWB with DATA ID, ex: F-D0047-001
    """
    logging.INFO('Update DATA ID: {}'.format(data_id))
    if not APP_KEY:
        logging.ERROR('Lack of APP KEY')
        raise LackKeyError
    url = 'http://opendata.cwb.gov.tw/opendataapi?dataid={}&authorizationkey={}'.format(data_id, APP_KEY)
    response = urllib.request.urlopen(url)
    data = response.read()
    xml = data.decode('utf-8')
    soup = Soup(xml, 'lxml')
    driver = GraphDatabase.driver(NEO4J_DB_PATH, auth=basic_auth(NEO4J_DB_USER, NEO4J_DB_PW))
    session = driver.session()
    session.run("MATCH (r:Region {data_id:'" + data_id + "'})"
                "SET r.issue_time='" + soup.find('issuetime').string.strip() + "'")

    for location in soup.find_all('location'):
        for e in location.find_all('weatherelement'):
            if e.elementname.string.strip() == 'WeatherDescription':
                descriptions = e
        session.run("MATCH (t:Town {geocode:'" + location.geocode.string.strip() + "'})"
                    "SET t.brief='" + brief(descriptions) + "'")


def brief(descriptions):
    """Shorten the 3 day weather description into a text message (75 letters)
    """
    # TODO: Implement the brief message

    # list of 2016-09-03T09:00:00+08:00
    start_times = [e.string.strip() for e in descriptions.find_all('starttime')]
    end_times = [e.string.strip() for e in descriptions.find_all('endtime')]

    # list of 多雲。 降雨機率 10%。 溫度攝氏25度。 舒適。 偏北風 平均風速0至1級(每秒1公尺)。 相對濕度為73%。
    values = [e.string.strip() for e in descriptions.find_all('value')]
    return values[0]

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='LINE %(lineno)-4d  %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('LINE %(lineno)-4d : %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    for dir_path, dir_names, files in os.walk(os.path.join(os.curdir, 'data')):
        for file in files:
            init_nodes_from_xml(os.path.join(dir_path, file))

