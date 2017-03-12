import midi
from customNote import CustomNote


def load(path):
    midifile = midi.read_midifile(path)
    noteEvents = []
    #print midifile
    if midifile.format:  # format=1: only MidiOn events
        print midi.read_midifile(path)
        for event in midi.read_midifile(path)[1]:
            if (type(event) == midi.events.NoteOnEvent and event.data[1] >= 1):
                noteEvents.append(event)
            if (type(event) == midi.events.NoteOnEvent and event.data[1] == 0):
                noteEvents.append(midi.NoteOffEvent(tick=event.tick, pitch=event.data[0]))
    else:

        for event in midi.read_midifile(path)[0]:
            if ((type(event) == midi.events.NoteOnEvent and event.data[1] >= 1 )or type(event) == midi.events.NoteOffEvent):
                noteEvents.append(event)
            if (type(event) == midi.events.NoteOnEvent and event.data[1] == 0):
                noteEvents.append(midi.NoteOffEvent(tick=event.tick, pitch=event.data[0]))

    return extractNotes(noteEvents, midifile.format), midifile.resolution, midifile.format


def extractNotes(rawList, format):
    openNotes = []
    closedNotes = []
    timeInTrack = 0
    if (format):
        for event in rawList:
            timeInTrack += event.tick
            if (event.data[1]):
                note = CustomNote(val=event.data[0], vel=event.data[1], len=None, pos=timeInTrack)
                openNotes.append(note)
            else:
                # search openNotes list and close the most recent note of the same value
                for openNote in openNotes:
                    if (openNote.val == event.data[0]):
                        openNote.len = timeInTrack - openNote.pos
                        closedNotes.append(openNote)
                        openNotes.remove(openNote)
    else:
        for event in rawList:
            timeInTrack += event.tick
            if (type(event) == midi.events.NoteOnEvent):
                note = CustomNote(val=event.data[0], vel=event.data[1], len=None, pos=timeInTrack)
                openNotes.append(note)

            if (type(event) == midi.events.NoteOffEvent):
                # search openNotes list and close the most recent note of the same value
                for openNote in openNotes:
                    if (openNote.val == event.data[0]):
                        openNote.len = timeInTrack - openNote.pos
                        closedNotes.append(openNote)
                        openNotes.remove(openNote)

    return closedNotes
