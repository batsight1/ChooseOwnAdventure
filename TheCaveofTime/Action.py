#Action Classs
#Pg     To      Text
class Action:
    def __init__(self,_text,_to):
        self.text = _text
        self.to = _to
    
    def GetText(self):
        return self.text
    def GetTo(self):
        return self.to