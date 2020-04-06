from random import randint
import time


def getRandomDoorOption():
    options = ['goat', 'car']
    selected = randint(0, 1)
    return options[selected]


def getDoors():
    doors = {
        'No 1': 'goat',
        'No 2': 'goat',
        'No 3': 'goat'
    }

    random_door = randint(1, 3)
    doors['No '+str(random_door)] = 'car'

    return doors


def guessDoor(change_decision):
    # the doors get setup
    doors = getDoors()

    # the guesser comes into the room
    options = ['No 1', 'No 2', 'No 3']
    guess_num = randint(0, 2)
    choosen_door_guess = options[guess_num]

    # do you want to change your guess?
    if change_decision == True:
        # remove a random goat door
        while len(doors) == 3:
            random_door = randint(1, 3)
            if doors['No '+str(random_door)] == 'goat':
                del doors['No '+str(random_door)]

        # guess again!
        guess_num = randint(0, 1)
        choosen_door_guess = list(doors.keys())[guess_num]

    # the unveal!!!
    if doors[choosen_door_guess] == 'car':
        # print('You won a car!!!')
        return 1
    else:
        # print('sorry, its a goat...')
        return 0


def testWhatsBetter():
    # lets test it 1000 times
    won_when_change_decision = 0
    won_when_NOT_change_decision = 0

    tries = 1
    while tries < 100:
        won_when_change_decision += guessDoor(True)
        won_when_NOT_change_decision += guessDoor(False)
        tries += 1

    print('Result:')
    print('won_when_change_decision: ' +
          str(round(won_when_change_decision/float(tries), 3)*100)+'%')
    print('won_when_NOT_change_decision: ' +
          str(round(won_when_NOT_change_decision/float(tries), 3)*100)+'%')


def testMultipleTimes():
    while True:
        testWhatsBetter()
        time.sleep(1)


testMultipleTimes()
