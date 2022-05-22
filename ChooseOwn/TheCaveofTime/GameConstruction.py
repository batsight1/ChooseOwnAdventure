#This is where the Events are made and saved
from Event import Event
from Action import Action
from JSON_Stuff import*
import os

EventList = {} #Dictionary
pathsEvents = pathsData+"EventsTXT\\"
Actions = {}

def ActionsHandling():
    f = open(pathsData+"Actions.txt","r")
    for x in f:
        #Breaking down line
        _string = x
        _string = _string.split("\t")
        _key = int(_string[0])
        _to = int(_string[1])
        if(len(_string)==3):
            _text = _string[2][:-1]
        else:
            _text = ""
        _action = Action(_text, _to)
        if(Actions.get(_key)==None):
            Actions[_key] = [_action]
        else:
            Actions[_key].append(_action)
    #If Dictionary doesnt have key create key, if it does then append to Dictionary value
    f.close()

list = os.listdir(pathsEvents) #List of text files
ActionsHandling()

#Create Event
for txt in list:
    f = open(pathsEvents+txt,"r")
    _passage = f.read()
    _key = int(txt[:-4])
    _event = Event(_passage,Actions.get(_key,[]))
    f.close()
    EventList[_key] = _event

#Save Events
SaveDictJSON(EventList, "data")

