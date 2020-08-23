from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

class importNBAData():
    def __init__(self, season, year):
        url = "https://www.basketball-reference.com/" + season + "/NBA_" + year + "_totals.html"
        html = urlopen(url)
        soup = BeautifulSoup(html, features="html.parser")

        # use findALL() to get the column headers, where tr is code for table row in html
        soup.findAll('tr', limit=2)
        # use getText()to get the column headers we need into a list
        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
        # remove the ranking, just category
        headers = headers[1:]

        rows = soup.findAll('tr')[1:]
        player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

        self.stats = pd.DataFrame(player_stats, columns=headers)
        self.stats.reset_index()
        self.stats.set_index('Player', inplace=True)

