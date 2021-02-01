# Class representing a football team


class Team:
    def __init__(self, name: str, fgoals: int, agoals: int):
        self.name = name
        self.fgoals = fgoals
        self.agoals = agoals

    def getgoaldiff(self):
        diff = self.fgoals - self.agoals
        return -diff if diff < 0 else diff

    def __str__(self):
        return self.name + ', goal differential: ' + str(self.getgoaldiff())
