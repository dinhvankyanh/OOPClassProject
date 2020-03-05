'''
Created on Mar 5, 2020

@author: Anh Dinh
'''
class Team:
    def __init__(self, teamName, activity):
        self.teamName = teamName
        self.activity = activity
        
    def toString(self):
        return "Team name = " + self.teamName + ", activity = " + self.activity 
      