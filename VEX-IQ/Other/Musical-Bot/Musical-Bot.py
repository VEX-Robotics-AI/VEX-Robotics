from vex import Brain, NoteType


# Jingle Bells song
jingle_bells_song = [
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.5],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.5],
    [NoteType.E, 4, 0.25],
    [NoteType.G, 4, 0.25],
    [NoteType.C, 4, 0.25],
    [NoteType.D, 4, 0.25],
    [NoteType.E, 4, 1],
    [NoteType.F, 4, 0.25],
    [NoteType.F, 4, 0.25],
    [NoteType.F, 4, 0.25],
    [NoteType.F, 4, 0.25],
    [NoteType.F, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.D, 4, 0.25],
    [NoteType.D, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.D, 4, 0.5],
    [NoteType.G, 4, 0.5],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.5],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.5],
    [NoteType.E, 4, 0.25],
    [NoteType.G, 4, 0.25],
    [NoteType.C, 4, 0.25],
    [NoteType.D, 4, 0.25],
    [NoteType.E, 4, 1],
    [NoteType.F, 4, 0.25],
    [NoteType.F, 4, 0.25],
    [NoteType.F, 4, 0.25],
    [NoteType.F, 4, 0.25],
    [NoteType.F, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.G, 4, 0.25],
    [NoteType.G, 4, 0.25],
    [NoteType.F, 4, 0.25],
    [NoteType.D, 4, 0.25],
    [NoteType.C, 4, 1]
]

# Happy Birthday song
happy_birthay_song = [
    [NoteType.G, 3, 0.125],
    [NoteType.G, 3, 0.125],
    [NoteType.A, 3, 0.25],
    [NoteType.G, 3, 0.25],
    [NoteType.C, 4, 0.25],
    [NoteType.B, 3, 0.5],
    [NoteType.G, 3, 0.125],
    [NoteType.G, 3, 0.125],
    [NoteType.A, 3, 0.25],
    [NoteType.G, 3, 0.25],
    [NoteType.D, 4, 0.25],
    [NoteType.C, 3, 0.5],
    [NoteType.G, 3, 0.125],
    [NoteType.G, 3, 0.125],
    [NoteType.G, 4, 0.25],
    [NoteType.E, 4, 0.25],
    [NoteType.C, 4, 0.125],
    [NoteType.C, 4, 0.125],
    [NoteType.B, 3, 0.25],
    [NoteType.A, 3, 0.25],
    [NoteType.F, 4, 0.125],
    [NoteType.F, 4, 0.125],
    [NoteType.E, 4, 0.25],
    [NoteType.C, 4, 0.25],
    [NoteType.D, 4, 0.25],
    [NoteType.C, 4, 0.5]
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
play_song(happy_birthay_song)
