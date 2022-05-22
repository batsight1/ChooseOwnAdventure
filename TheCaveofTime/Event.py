#Event Class
from Action import Action
from json import JSONEncoder
import json

class Event:
    def __init__(self,_passage,_actions):
        self.passage = _passage
        self.actions = _actions
        #If no actions then it is The End
        #If no text in Action then "Next"
    
    def GetPassage(self):
        return self.passage
    def GetAction(self,i):
        return self.actions[i]
    def GetActions(self):
        return self.actions
    def GetActionText(self,i):
        return self.actions[i].GetActionText()
    def GetActionTo(self,i):
        return self.actions[i].GetActionTo()
    def SetActions(self,_actions):
        self.actions = _actions
    def SetPassage(self,_passage):
        self.passage = _passage
    def AddActions(self,_action):
        self.actions.append(_action)
    def IsEnd(self):
        if(len(self.actions)==0):
            return True
        else:
            return False
