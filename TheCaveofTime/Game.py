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

#Input Handling
def InputValid(_input):
    if(_input in ["q",'s','l','r',"",'1','2','3','4','5','6','7','8','9']):
        return True
    else:
        return False

def InputLoop(_input):
    while not InputValid(_input):
        print("Invalid")
        _input = input("Input: ")
        InputLoop(_input)
    return _input

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

def GameLoop():
    global current
    while not gameover:
        PrintPassage(current)
        if EventIsEnd(GetEvent(current)): #Check if it is The End
            break
        PrintActions(GetActions(current))

        ans = InputLoop(input("Input: "))
        if(ans=="q"): #Quit
            print("Game Quit")
            break
        elif(ans in ['1','2','3','4','5','6','7','8','9']):
            ans = int(ans) - 1
            if(ans>=len(GetActions(current))):
                break
            _action = GetAction(GetEvent(current),ans)
            current = GetActionTo(_action)
        elif(ans=="s"): #Save
            break
        elif(ans=="l"): #Load
            break
        elif(ans=="r"): #Restart
            current = 2
        elif(ans==""): #Continue
            if(len(GetActions(current))==1):
                ans = 0
                _action = GetAction(GetEvent(current),ans)
                current = GetActionTo(_action)
            else:
                break
        else:
            break
        
        cls()
    if(gameover):
        print("This is the End")

def MainMenu():
    print("Main Menu")
    print("Welcome to the Choose Your Own Adventure Game\n Please Select the Game you would like to play")
    print("1) The Cave of Time")
    #QuestionLoop
    while True:
        ans = InputLoop("Enter Game")
        if(ans=="q"): #Quit
            print("Game Quit")
            break
        elif(ans=="1"):
            print("The Cave of Time selected")
            break

#GameLoop()
MainMenu()


    