from JSON_Stuff import*
#T#his is where the Game is played
#Note:Make your own input function

#Variables
EventList = {}
EventList = ReadDictJSON("data") #Load Events

#Methods
def GetEvent(i):
    return EventList[i]
def GetPassage(i):
    return GetEvent(i).GetPassage()

#Find a passage
print("Finding a Passage")
print("Enter Passage Number:")
x = int(input())
print(GetPassage(x))