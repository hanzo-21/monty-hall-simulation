import random
import matplotlib.pyplot as plt

totalNumberOfExperment = 5
sucessfullExperment = [0]*2
xlabel= ["50 - 50", "33 - 66"]
widthOfBar = 0.35


def randomDoor(initialDoorSet):
    doorList = list(initialDoorSet)
    #print(type(doorList),doorList)
    random.shuffle(doorList)
    RandDoor = set(doorList.pop(0))
    return RandDoor

def openUnchosedDoorWithNocar(initialDoorSet,putCarIn,chooseDoor):
    doorset = initialDoorSet - (putCarIn | chooseDoor)
    doorList = list(doorset)
    random.shuffle(doorList)
    RandDoor = set(doorList.pop(0))
    return RandDoor

def chooseDoorAtRandomForSecondTime(initialDoorSet,openDoor):
    doorList = list (initialDoorSet - openDoor)
    random.shuffle(doorList)
    randDoor = set(doorList.pop(0))
    return randDoor

def MontiHallExperiment66():

    initialDoorSet = {'X','Y','Z'}
    print("Monti: There are 3 doors", initialDoorSet,"One of Them hsa a car behind it. but which one?")

    putCarIn = randomDoor(initialDoorSet)
    #print("car was in ",str(putCarIn))

    chooseDoor = randomDoor(initialDoorSet)
    print("Sterling: I choose door ", str(chooseDoor))

    openDoor = openUnchosedDoorWithNocar(initialDoorSet=initialDoorSet,putCarIn=putCarIn,chooseDoor=chooseDoor)
    print("Monti: Well well, I'll open the door" ,str(openDoor),"and lucky you, this is empty.")
    print("Monti: So I ask you now. will you change your answer?")
     
    chooseDoor = initialDoorSet - chooseDoor - openDoor
    print("Sterling: I'm gonna do what's called a pro gamer move and choose door ",str(chooseDoor))

    if(putCarIn == chooseDoor ):
        print("CONGRATULATION!! YOU WON A CAR")
        return True
    else:
        print("sorry you didn't win")
        return False

def MontiHallExperiment33():

    initialDoorSet = {'X','Y','Z'}
    print("Monti: There are 3 doors", initialDoorSet,"One of Them hsa a car behind it. but which one?")

    putCarIn = randomDoor(initialDoorSet)
    #print("car was in ",str(putCarIn))

    chooseDoor = randomDoor(initialDoorSet)
    print("Sterling: I choose door ", str(chooseDoor))

    openDoor = openUnchosedDoorWithNocar(initialDoorSet=initialDoorSet,putCarIn=putCarIn,chooseDoor=chooseDoor)
    print("Monti: Well well, I'll open the door" ,str(openDoor),"and lucky you, this is empty.")
    print("Monti: So I ask you now. will you change your answer?")
    
    chooseDoor = chooseDoorAtRandomForSecondTime(initialDoorSet=initialDoorSet,openDoor=set(openDoor))
    print("Sterling: It's 50 - 50 so I choose ",str(chooseDoor))

    if(putCarIn == chooseDoor ):
        print("CONGRATULATION!! YOU WON A CAR")
        return True
    else:
        print("sorry you didn't win")
        return False

#for option A to not to change options
experimentNum=0
print("Conducting ",totalNumberOfExperment," experiments for optioin A")

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

print("Conducting ",totalNumberOfExperment," experiments for optioin A")

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
plt.bar(x=xlabel,height=sucessfullExperment,width= widthOfBar,label = "successfull predictions",hatch = '.',fill = False)
title = "Simulation of Monti Hall problem "+ str(totalNumberOfExperment) + " times"
plt.title(title,loc="center")
plt.xlabel("Methods used",loc="center")
plt.ylabel("Number of successfull experiment")
plt.legend()
plt.grid()
plt.show()