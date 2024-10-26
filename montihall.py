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

def chooseDoorAtRandomForSecondTime(initialDoorSet,openDoor):
    doorList = list (initialDoorSet - openDoor)
    random.shuffle(doorList)
    randDoor = doorList.pop(0)
    return randDoor

def MontiHallExperiment66():

    initialDoorSet = {'X','Y','Z'}
    print("there are 3 doors", initialDoorSet)

    putCarIn = randomDoor(initialDoorSet)
    chooseDoor = randomDoor(initialDoorSet)
    print("Out of them we choose door ", chooseDoor)

    openDoor = openUnchosedDoorWithNocar(initialDoorSe=initialDoorSet,putCarIn=set(putCarIn),chooseDoor=set(chooseDoor))
    print("The host then opens the door " ,openDoor," which was empty.")
    print("The host then offers us as choice to changes our initial answer\nWe decided to change our choice")
    
    chooseDoor = initialDoorSet - chooseDoor - openDoor
    print("Now, we choose to open door ",openDoor)
    # check if sets check if open door and choosen door are same

    if(putCarIn == chooseDoor ):
        print("CONGRATULATION!! YOU WON A CAR")
        return True
    else:
        print("sorry you didn't win")
        return False

def MontiHallExperiment33():

    initialDoorSet = {'X','Y','Z'}
    print("there are 3 doors", initialDoorSet)

    putCarIn = randomDoor(initialDoorSet)
    chooseDoor = randomDoor(initialDoorSet)
    print("Out of them we choose door ", chooseDoor)

    openDoor = openUnchosedDoorWithNocar(initialDoorSe=initialDoorSet,putCarIn=set(putCarIn),chooseDoor=set(chooseDoor))
    print("The host then opens the door " ,openDoor," which was empty.")
    print("The host then offers us as choice to changes our initial answer\nWe decided not to change our choice")
    
    chooseDoor = chooseDoorAtRandomForSecondTime(initialDoorSet=initialDoorSet,openDoor=set(openDoor))
    print("Now, we choose to open door ",chooseDoor)
    # check if sets check if open door and are same

    if(putCarIn == chooseDoor ):
        print("CONGRATULATION!! YOU WON A CAR")
        return True
    else:
        print("sorry you didn't win")
        return False

totalNumberOfExperment = 1000
sucessfullExperment = [0]*2
xlabel= ["Success from option A", "Success from option B"]

#for option A to not to change options
experimentNum = 0
while(experimentNum < totalNumberOfExperment):

    print("=====================================================")
    print("Experiment number ",experimentNum+1)

    result = MontiHallExperiment33()

    if(result == True):
        sucessfullExperment[0]+=1
       
    experimentNum+=1
    print("=====================================================")

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

# plot the data on to set

plt.figure(figsize=(10,6))
plt.bar(x=xlabel,y=sucessfullExperment,width= 20,lable = "successfull predictions")