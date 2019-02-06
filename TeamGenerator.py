# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:55:41 2019

@author: Micah
"""
from random import choice

playerList = []
teamList = []

playerName = ""
teamName = ""
teamCounter = 0

while playerName != "done":
    playerName = input("Enter a player name (type 'done' when all players are finished): ")
    
    if playerName != "done":
        playerList.append(playerName)

teamNumber = int(input("We'll pick two random team names from the choices you give. How many choices do you want to give? "))

while teamCounter < teamNumber:
    teamName = input("Enter a team name: ")
    teamList.append(teamName)
    teamCounter += 1


teamA = []
teamB = []

while len(playerList) > 0:
    playerA = choice(playerList)
    teamA.append(playerA)
    playerList.remove(playerA)
    
    if playerList == []:
        break
    
    playerB = choice(playerList)
    teamB.append(playerB)
    playerList.remove(playerB)
    
firstTeam = choice(teamList)
teamList.remove(firstTeam)
secondTeam = choice(teamList)
teamList.remove(secondTeam)

print('\nHere are your teams:\n')
print(firstTeam, teamA)
print(secondTeam, teamB)