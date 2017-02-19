import midi

def writeList(customList, res):
    # Instantiate a MIDI Pattern (contains a list of tracks)
    pattern = midi.Pattern(resolution=res)
    # Instantiate a MIDI Track (contains a list of MIDI events)
    track = midi.Track()
    # Append the track to the pattern
    pattern.append(track)
    # Instantiate a MIDI note on event, append it to the track
    timeInTrack = 0
    for note in customList:
        #timeInTrack += note.pos
        on = midi.NoteOnEvent(tick = timeInTrack, velocity = note.vel, pitch = note.val)
        track.append(on)
        # Instantiate a MIDI note off event, append it to the track
        off = midi.NoteOffEvent(tick = (timeInTrack + note.len), pitch = note.val)
        track.append(off)
    # Add the end of track event, append it to the track
    eot = midi.EndOfTrackEvent(tick=1)
    track.append(eot)
    # Print out the pattern
    print pattern
    # Save the pattern to disk
    midi.write_midifile("rebuilt.mid", pattern)
