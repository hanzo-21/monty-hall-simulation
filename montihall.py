import numpy as np
import random
import matplotlib.pyplot as plt

def randomDoor(initialDoorSet):
    doorList = list(initialDoorSet)
    print(type(doorList),doorList)
    random.shuffle(doorList)
    RandDoor = doorList.pop(0)
    return RandDoor

def openUnchosedDoorWithNocar(initialDoorSet,putCarIn,chooseDoor):
    doorset = initialDoorSet - (putCarIn | chooseDoor)
    doorList = list(doorset)
    random.shuffle(doorList)
    RandDoor = doorList.pop(0)
    return RandDoor

def MontiHallExperiment66():

    initialDoorSet = {'X','Y','Z'}
    print("there are 3 doors", initialDoorSet)

    putCarIn = randomDoor(initialDoorSet)
    chooseDoor = randomDoor(initialDoorSet)
    print("Out of them we choose door ", chooseDoor)

    openDoor = openUnchosedDoorWithNocar(initialDoorSe=initialDoorSet,putCarIn=set(putCarIn),chooseDoor=set(chooseDoor))
    print("The host then opens the door " ,openDoor," which was empty.")
    print("The host then offers us as choice to changes our initial answer\nWe decided to change our choice")
    
    openDoor = initialDoorSet - chooseDoor - openDoor
    print("Now, we choose to open door ",openDoor)
    # check if sets check if open door and are same

    if(openDoor == chooseDoor ):
        print("CONGRATULATION!! YOU WON A CAR")
        return True
    else:
        print("sorry you didn't win")
        return False


# need to write for option a 

totalNumberOfExperment = 1000
sucessfullExperment = [0]*2



#for option A to not to change options
experimentNum = 0
while(experimentNum < totalNumberOfExperment):
    

    experimentNum+=1

#for option B to choose to change options
experimentNum = 0

while(experimentNum < totalNumberOfExperment):

    print("=====================================================")
    print("Experiment number ",experimentNum+1)

    result = MontiHallExperiment66()

    if(result == True):
        sucessfullExperment[1]+=1
       
    experimentNum+=1
    print("=====================================================")

    


