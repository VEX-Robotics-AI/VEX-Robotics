from vex import Brain, TimeUnits


class Autopilot:
    def __init__(self):
        self.brain = Brain()


if __name__ == 'TBD':
    AUTOPILOT = Autopilot()

    AUTOPILOT.brain.sound.play(
        3,   # note
        3,   # octave
        1,   # duration
        TimeUnits.SEC   # timeUnit
    )
