from JSON_Stuff import*
import os
#T#his is where the Game is played
#Note:Make your own input function
def cls(): #To Clear Console
    os.system('cls' if os.name=='nt' else 'clear')

#Variables
EventList = {}
EventList = ReadDictJSON("data") #Load Events
current = 2
gameover = False

#Methods
def GetEvent(i):
    return EventList[i]
def GetPassage(i):
    return GetEvent(i).GetPassage()
def GetActions(i):
    return GetEvent(i).GetActions()
def GetAction(_event,i):
    return _event.GetAction(i)
def GetActionText(_action):
    return _action.GetText()
def GetActionTo(_action):
    return _action.GetTo()
def EventIsEnd(_event):
    return _event.IsEnd()
def PrintPassage(i):
    print(GetPassage(i))
def PrintActions(_actions):
    if(len(_actions)==1):
        print("Continue")
    else:
        for i in range(len(_actions)):
            print(str(i+1)+") If you "+GetActionText(_actions[i]))

#current = GameLoop(current)
#current = GameLoop(current)
current = 92
#GameLoop
while not gameover:
    PrintPassage(current)
    if EventIsEnd(GetEvent(current)): #Check if it is The End
        gameover = True
        break
    PrintActions(GetActions(current))
    ans = input("Action: ")
    if(ans=="q"):
        break
    elif(ans==""):
        if(len(GetActions(current))==1):
            ans = 0
    else:
        ans = int(ans) - 1
    current = GetActionTo(GetAction(GetEvent(current),ans))
    cls()

if(gameover):
    print("This is the End")