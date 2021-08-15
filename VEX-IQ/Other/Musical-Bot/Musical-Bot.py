from vex import Brain, NoteType


# init Jingle Bells song
jingle_bells_song = [
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.5],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.5],
    # homework: add more notes to the song
]


# init the VEX IQ brain
brain = Brain()


# define a function to play a song
def play_song(song):
    for note in song:
        note_type = note[0]
        octave = note[1]
        note_value = note[2]
        brain.sound.play(note_type, octave, note_value)


# main program
play_song(jingle_bells_song)
