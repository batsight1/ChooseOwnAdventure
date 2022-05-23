def InputHandle(_input):
    if(ans==["q",'s','l','r']):
        return ans
    elif(ans==""):
        return ans
    elif(ans in ['1','2','3','4','5','6','7','8','9']):
        return int(ans)
    else:
        InputHandle(input("Input: "))

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

ans = InputLoop(input("Input: "))
print(ans)