"""drive.google.com/file/d/10c7uscsGrdhtjqn0OzDdRyv48htE5BuY"""


# flake8: noqa: F401
# pylint: disable=import-error,unused-import


from vex import (Brain, SoundType,

                 Ports,

                 Controller,

                 Inertial,
                 AxisType, XAXIS, YAXIS, ZAXIS,
                 OrientationType, PITCH, ROLL, YAW,

                 Motor,
                 BrakeType, COAST, BRAKE, HOLD,
                 CurrentUnits,
                 DirectionType, FORWARD, REVERSE,
                 TorqueUnits,
                 TurnType, LEFT, RIGHT,
                 VelocityUnits, RPM, DPS,

                 Bumper,
                 ColorSensor,
                 Distance, ObjectSizeType,
                 Gyro, GyroCalibrationType,
                 Optical, LedStateType, GestureType,
                 Sonar,
                 Touchled, FadeType,
                 Vision, VisionObject,

                 TimeUnits, SECONDS, MSEC, wait,

                 PERCENT,
                 RotationUnits, DEGREES, TURNS,
                 DistanceUnits, MM, INCHES,

                 MotorGroup, DriveTrain, SmartDrive)

from random import randint
