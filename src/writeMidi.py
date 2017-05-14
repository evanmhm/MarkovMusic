import midi


def writeList(customList, res, format):
    # Instantiate a MIDI Pattern (contains a list of tracks)
    pattern = midi.Pattern(resolution=res)
    # Instantiate a MIDI Track (contains a list of MIDI events)
    track = midi.Track()
    # Append the track to the pattern
    pattern.append(track)
    # Instantiate a MIDI note on event, append it to the track
    prevPos = -1
    prevLen = 0
    multinoteIndex = 0
    if (format):
        for note in customList:
            on = midi.NoteOnEvent(tick=0, velocity=note.vel, pitch=note.val)
            track.append(on)
            # Instantiate a MIDI note off event, append it to the track
            off = midi.NoteOffEvent(tick=note.len, pitch=note.val)
            track.append(off)
    else:
        for note in customList:
            if (note.pos < prevPos + prevLen):
                on = midi.NoteOnEvent(tick=note.pos - prevPos, velocity=note.vel, pitch=note.val)
                multinoteIndex += 1
                track.insert(len(track) - multinoteIndex, on)
                off = midi.NoteOffEvent(tick=0, pitch=note.val)
                track.append(off)
            else:
                multinoteIndex = 0
                if (prevPos == -1):
                    prevPos = 0
                on = midi.NoteOnEvent(tick=note.pos - (prevPos + prevLen),
                                      velocity=note.vel, pitch=note.val)
                track.append(on)
                # Instantiate a MIDI note off event, append it to the track
                off = midi.NoteOffEvent(tick=(0 + note.len), pitch=note.val)
                track.append(off)
            prevPos = note.pos
            prevLen = note.len
    # Add the end of track event, append it to the track
    eot = midi.EndOfTrackEvent(tick=1)
    track.append(eot)

    # Save the pattern to disk
    midi.write_midifile("rebuilt.mid", pattern)
