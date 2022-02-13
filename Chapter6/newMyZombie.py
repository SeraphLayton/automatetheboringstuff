import zombiedice
import random

class MyZombieRandom:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll() # first roll

        
        while True:
            r = random.randint(0,1)
            if r == 1:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MyZombie2Brainer:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        
        diceRollResults = zombiedice.roll() # first roll

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains == 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break


class MyZombie2Shotgun:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        
        diceRollResults = zombiedice.roll() # first roll

        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MyZombie1to4:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        
        diceRollResults = zombiedice.roll() # first roll

        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            for i in range(random.randint(1, 4)):
                if shotguns == 2:
                    break
                diceRollResults = zombiedice.roll()
            break


class MyZombieShotOverBrain:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        
        diceRollResults = zombiedice.roll() # first roll

        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']

            if shotguns <= brains:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break



zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    zombiedice.examples.MonteCarloZombie(name='Monte', riskiness=53, numExperiments=100),
    MyZombieRandom(name='My Zombie Bot Random'),
    MyZombie2Brainer(name='My Zombie Bot 2Brainer'),
    MyZombie2Shotgun(name='My Zombie Bot 2Shotgun'),
    MyZombie1to4(name='My Zombie Bot 1to4'),
    MyZombieShotOverBrain(name='My Zombie Bot ShotOverBrain'),
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
