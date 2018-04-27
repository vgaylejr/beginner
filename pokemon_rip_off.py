# So both the computer and the player starts off with the same amount of health
#write the moves first then combine them into a menu
#combine the moves? Think we can make it more player friendly? was looking at Tkinter. You know how to use it? sort of.
#ive done some stuff in it before. nothing too fancy though.ok. lets keep it basic then. lets add GUI after it works

#imports random Class for random number generation
import random

#initializes player and computer health
playerHealth = 100
computerHealth = 100

#moves
small= random.randint(18,25)
big = random.randint(10,35)
heal = random.randint(10,20)

#computer move
def computerMove():
    comMove = random.randint(1,3)
    if comMove == 1:
        global playerHealth
        playerHealth = playerHealth - small
        print(playerHealth)

    if comMove == 2:
        global playerHealth
        playerHealth = playerHealth - big
        print(playerHealth)

    if comMove == 3:
        global computerHealth
        computerHealth = computerHealth + heal
        if computerHealth > 100:
            computerHealth = 100
        print(playerHealth)

while playerHealth > 0 and computerHealth> 0:
    playerMove = input('select your move')
    if playerMove == 1:
        computerHealth = computerHealth - small
        computerMove()
        print('Player has {} health left'.format(playerHealth))
        print ('Computer has {} health left'.format(computerHealth))
    elif playerMove == 2:
        computerHealth = computerHealth - big
        computerMove()
        print('Player has {} health left'.format(playerHealth))
        print ('Computer has {} health left'.format(computerHealth))
    elif playerMove == 3:
        playerHealth = playerHealth + heal
        if playerHealth > 100:
            playerHealth = 100
        computerMove()
        print('Player has {} health left'.format(playerHealth))
        print ('Computer has {} health left'.format(computerHealth))
    else:
        print('Please type 1 to attack, 2 to attack big, or 3 to heal')
        continue
