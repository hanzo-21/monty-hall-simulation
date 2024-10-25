import numpy as np
import random
import matplotlib.pyplot as plt

def randomDoor(initialDoorSet):
    doorList = list(initialDoorSet)
    print(type(doorList),doorList)
    random.shuffle(doorList)
    RandDoor = doorList.pop(0)
    return RandDoor

def openUnchosedDoorWithNocar(initialDoorSet,putCarIn,chooseDoor); 
    doorset = initialDoorSet - (putCarIn | chooseDoor)
    doorList = list(doorset)
    random.shuffle(doorList)
    RandDoor = doorList.pop(0)
    return RandDoor


######

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

    


