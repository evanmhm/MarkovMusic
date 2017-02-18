import midi
from customNote import CustomNote

def load(path):
    midifile = midi.read_midifile(path)
    noteEvents = []
    if midifile.format:
        for event in midi.read_midifile(path)[1]:
            if (type(event) == midi.events.NoteOnEvent or type(event) == midi.events.NoteOffEvent):
                noteEvents.append(event)
    else:
        for event in midi.read_midifile(path)[0]:
            if (type(event) == midi.events.NoteOnEvent or type(event) == midi.events.NoteOffEvent):
                noteEvents.append(event)

    return extractNotes(noteEvents)

def extractNotes(rawList):
    openNotes = []
    closedNotes = []
    timeInTrack = 0
    for event in rawList:
        timeInTrack += event.tick
        if (type(event) == midi.events.NoteOnEvent):
            note = CustomNote(val = event.data[0], vel = event.data[1], len = None, pos = timeInTrack)
            openNotes.append(note)

        if (type(event) == midi.events.NoteOffEvent):
            #search openNotes list and close the most recent note of the same value
            for openNote in openNotes:
                if (openNote.val == event.data[0]):
                    openNote.len = timeInTrack - openNote.pos
                    closedNotes.append(openNote)
                    openNotes.remove(openNote)


    return closedNotes
