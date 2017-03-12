import midi
from customNote import CustomNote

def listToString(customList):
    output = ''

    for note in customList:
        output += str(note.pos) + ',' + str(note.len) + ',' + str(note.val) + ',' + str(note.vel) + ', '

    return output

def stringToList(stringList):
    output = []
    splitOne = stringList.split(' ')
    for note in splitOne:
        splitString = stringList.split(',')
        output.append(CustomNote(pos=int(splitString[0]), len=int(splitString[1]), val=int(splitString[2]), vel=int(splitString[3])))

    return output
