import random # imports random class for random number generation
playerHealth = 100
computerHealth = 100 # initializes player and computer health
#moves
small= random.randint(18,25)
big = random.randint(10,35)
heal = random.randint(10,20)

#main run for program
while playerHealth > 0 and computerHealth> 0:
    playerMove = int(input('select your move'))
    if playerMove == 1:
        computerHealth = computerHealth - small
        comMove = random.randint(1,3)
        if comMove == 1:
            playerHealth = playerHealth - small
        elif comMove == 2:
            playerHealth = playerHealth - big
        elif comMove == 3:
                computerHealth = computerHealth + heal
        print('Player has {} health left'.format(playerHealth))
        print ('Computer has {} health left'.format(computerHealth))
    if playerMove == 2:
        computerHealth = computerHealth - big
        comMove = random.randint(1,3)
        if comMove == 1:
            playerHealth = playerHealth - small
        elif comMove == 2:
            playerHealth = playerHealth - big
        elif comMove == 3:
                computerHealth = computerHealth + heal
        print('Player has {} health left'.format(playerHealth))
        print ('Computer has {} health left'.format(computerHealth))
    if playerMove == 3:
        playerHealth = playerHealth + heal
        if playerHealth > 100:
            playerHealth = 100
        comMove = random.randint(1,3)
        if comMove == 1:
            playerHealth = playerHealth - small
        elif comMove == 2:
            playerHealth = playerHealth - big
        elif comMove == 3:
                computerHealth = computerHealth + heal
        print('Player has {} health left'.format(playerHealth))
        print ('Computer has {} health left'.format(computerHealth))
    else:
        print('Please type 1 to attack, 2 to attack big, or 3 to heal')
        continue
