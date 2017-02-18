import midi

def load(path):
    midifile = midi.read_midifile(path)
    organizedList = []
    if midifile.format:
        for event in midi.read_midifile(path)[1]:
            if (type(event) == midi.events.NoteOnEvent):
                organizedList.append(event)
    else:
        for event in midi.read_midifile(path)[0]:
            if (type(event) == midi.events.NoteOnEvent):
                organizedList.append(event)

    return organizedList
