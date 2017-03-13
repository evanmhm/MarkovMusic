import midi
from customNote import CustomNote

def listToString(customList):
    output = ''

    for note in customList:
        output += str(note.len) + ',' + str(note.val) + ',' + str(note.vel) + ' '

    return output

def stringToList(stringList):
    output = []
    splitOne = stringList.split(' ')
    trackPos = 0
    for note in splitOne:
        splitString = note.split(',')
        if len(splitString) > 1 :
            output.append(CustomNote(pos=trackPos, len=int(splitString[0]), val=int(splitString[1]), vel=int(splitString[2])))
            trackPos += int(splitString[0])
            

    return output
