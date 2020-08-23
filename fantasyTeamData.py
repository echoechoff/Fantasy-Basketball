import importNBAData
import numpy
import pprint
import pandas

class fantasyTeamData():
    def __init__(self, teamRoster, statCatergories):
        playoffs2020data = importNBAData.importNBAData("playoffs", "2020")

        self.stats = playoffs2020data.stats.loc[teamRoster, statCatergories]
        self.stats[statCatergories] = self.stats[statCatergories].astype(int)
        self.stats.loc["Total"] = self.stats.sum(axis=0)
        self.totalStats = self.stats.loc["Total"]
