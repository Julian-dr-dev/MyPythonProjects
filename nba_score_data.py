import printer as printer
from requests import get
from pprint import PrettyPrinter


BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()
def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

def getScoreboard():
    scoreboard = get_links()['currentScoreboard']
    data = get(BASE_URL + scoreboard).json()['games']

    printer.pprint(data.keys())




getScoreboard()



