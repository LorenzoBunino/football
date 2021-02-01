# Class describing a season of Premier League

import io

import pandas as pd

from football import Team


class Season:
    def __init__(self, rawdata):
        self.rawdata = pd.read_fwf(self.__rawdatacleanup(rawdata), index_col=0)

    @staticmethod
    def __rawdatacleanup(rawdata: str):
        lines = open(rawdata, 'r').readlines()
        for index, line in enumerate(lines):
            # if anything more than one dash is found, line is considered empty
            if '--' in line:  # alternative could be counting spaces/separators
                del lines[index]

        return io.StringIO('\n'.join(lines))

    def getteam(self, name: str):
        fgoals = self.rawdata.loc[self.rawdata['Team'] == name, 'F'].values[0]
        agoals = self.rawdata.loc[self.rawdata['Team'] == name, 'A'].values[0]
        return Team.Team(name, fgoals, agoals)

    def getmingoaldiffteam(self):
        mindiff_f_a_team = self.getteam(self.rawdata.loc[1.0, 'Team'])  # init
        for index, data in self.rawdata.iterrows():
            curr_team = self.getteam(data.Team)
            if curr_team.getgoaldiff() < mindiff_f_a_team.getgoaldiff():
                mindiff_f_a_team = curr_team

        return mindiff_f_a_team
