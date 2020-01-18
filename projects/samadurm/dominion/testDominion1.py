# -*- coding: utf-8 -*-
"""
Created on Thursday Jan 20 11:41 2020

@author: Micah Samaduroff
"""

from testUtility import *

#Set up the game

#Get player names and construct the player objects

## TEST SCENARIO!
# player_names = ["Annie", "*Ben", "*Carla"]
player_names = ["Annie"]
players = construct_players(player_names)

#number of curses and victory cards
num_victory_cards = get_num_curse_victory_cards(player_names)

num_cards = -10 + 10 * len(player_names)


#Game initialization data removed by Micah for refactoring
box = get_boxes(num_victory_cards)

supply_order = create_supply_order()

#Add 10 cards from the box to the supply
supply = add_to_supply(box)
supply = init_deck(supply, player_names, num_victory_cards, num_cards)

#initialize the trash
trash = []


#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)


#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)