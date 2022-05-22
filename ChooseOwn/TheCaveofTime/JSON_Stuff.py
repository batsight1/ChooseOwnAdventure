from Event import Event
from Action import Action
import os
import json

pathsData = "Data\\"

def EventToJSON(_event): #This Serializes Event Object
    _actions = _event.GetActions()
    for i in range(len(_actions)):
        _actions[i] = ActionToJSON(_actions[i])
    _event.SetActions(_actions)
    return json.dumps(_event.__dict__)

def ActionToJSON(_action):
    return json.dumps(_action.__dict__)

def JSONToEvent(_js):   #This Un-serializes Event Object
    _dic = json.loads(_js)
    return(Event(_dic['passage'],_dic['actions']))

def JSONToAction(_js):
    _dic = json.loads(_js)
    return(Action(_dic['text'], _dic['to']))

def SaveEventJSON(_event,_filename): #THis saves the individual Event Object, need to incorporate Action
    jsonFile = open(pathsData+_filename+".json", "w")
    jsonFile.write(EventToJSON(_event))
    jsonFile.close()

def SerialDict(_list): #This returns a Dictionary of Serialized Event Objects
    _serDict = {}
    for e in _list:
        _serial = EventToJSON(_list[e])
        _serDict[e] = _serial
    return _serDict

def SaveDictJSON(_list,_filename): #This saves the Dictionary of Serialized Event Objects as JSON
    EventList = SerialDict(_list) #serialize list
    jsonString = json.dumps(EventList)
    jsonFile = open(pathsData+_filename+".json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

def ReadDictJSON(_filename): 
    fileObject = open(pathsData+_filename+".json", "r")
    jsonContent = fileObject.read()
    fileObject.close()
    aList = json.loads(jsonContent) #Turns JSON to Dict of Serialized Event Objects
    _list = {}
    for e in aList:
        _serial = aList[e] #Serialized Event Object
        _list[int(e)]= JSONToEvent(_serial) #Un-serialized Event Object
    return _list

