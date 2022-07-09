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
    games = get(BASE_URL + scoreboard).json()['games']

    for game in games:
        homeTeam = game['hTeam']
        awayTeam = game['vTeam']
        clock = game['clock']
        period = game['period']


        print('=' * 80)
        print(f"{homeTeam['triCode']} vs {awayTeam['triCode']}")
        print(f"{period['current']} - {clock} ")
        print(f"{homeTeam['score']} - {awayTeam['score']}")


def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    for team in teams:
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']
        fieldPct = team['fgp']
        print(f"{name} - {nickname} - {ppg} - {fieldPct}")





get_stats()






