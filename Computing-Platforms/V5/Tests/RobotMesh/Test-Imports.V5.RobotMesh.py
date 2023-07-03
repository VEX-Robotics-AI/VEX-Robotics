"""robotmesh.com/studio/64751878f47a886576b2ad43"""


# flake8: noqa: F401

# pylint: disable=import-error,pointless-statement,redefined-builtin,reimported
# pylint: disable=unused-import,wrong-import-position


# VEX module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacevex.html
# =====================================================================
from vex import (Device, TriDevice, V5DeviceType,

                 # Brain, BrainButton, BrainLcd, BrainSound, NoteType,

                 # Ports,

                 # Controller, ControllerAxis, ControllerButton,

                 Motor,
                 # BrakeType,
                 # DirectionType, FORWARD, REVERSE,
                 TorqueUnits,
                 # TurnType, LEFT, RIGHT,
                 # VelocityUnits,

                 # Bumper,
                 # Colorsensor, ColorHue,
                 # Gyro, GyroCalibrationType,
                 # Sonar,
                 # Touchled, FadeType,

                 TimeUnits, SECONDS, wait,  # wait_for,

                 # PERCENT,
                 AnalogUnits,
                 DistanceUnits, MM, INCHES,
                 # RotationUnits, DEGREES, TURNS,

                 # INT29_MAX

                 RUMBLE_LONG, RUMBLE_PULSE, RUMBLE_SHORT,
                 STATUS_BAR_HEIGHT, SYSTEM_DISPLAY_HEIGHT, SYSTEM_DISPLAY_WIDTH,  # noqa: E501

                 staticmethod)


# MOTOR_GROUP module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacemotor__group.html
# ==============================================================================
from motor_group import MotorGroup


# DRIVETRAIN module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacedrivetrain.html
# ============================================================================
from drivetrain import Drivetrain


# SMARTDRIVE module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacesmartdrive.html
# ============================================================================
from smartdrive import Smartdrive


# TIMER module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacetimer.html
# =======================================================================
from timer import Timer


# SYS module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacesys.html
# =====================================================================
from sys import (clock,
                 maxint,
                 sleep,
                 run_in_thread,
                 wait_for,
                 exit,
                 gc,
                 getb,
                 heap,
                 putb,
                 thread_id)


# MATH module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacemath.html
# ======================================================================
from math import (
    # number theoretic and representation functions
    ceil, copysign, fabs, factorial, floor, fmod, frexp, fsum, isinf, isnan,
    ldexp, modf, trunc,

    # trigonometric functions
    acos, asin, atan, atan2, cos, hypot, sin, tan,

    # angular conversion
    degrees, radians, pi,

    # hyperbolic functions
    acosh, asinh, atanh, cosh, sinh, tanh,

    # power and logarithmic functions
    e, exp, log, log1p, log10, pow, sqrt,

    # misc/other
    is_prime,
)


# RANDOM module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacerandom.html
# ========================================================================
from random import randint, random, choice


# __BI module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespace____bi.html
# ========================================================================

# classes
# -------
object

bytearray

Exception
AssertionError

# functions
# ---------
abs
float
round
divmod
max
min
chr
int
str
dir
filter
globals
id
len
locals
map
ord
pow
range
sum
type
# pylint: disable=undefined-variable
ismain  # noqa: F821


# BUILT-INS module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacebuilt__ins.html
# ============================================================================
# (NOT APPLICABLE)


# DICT module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacedict.html
# ======================================================================
from dict import _Autobox, clear, keys, has_key, values, update  # noqa: E402


# FUNC module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacefunc.html
# ======================================================================
# from func import co_names, co_consts


# LIST module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacelist.html
# ======================================================================
from list import _Autobox, append, count, extend, index, insert, pop, remove  # noqa: E402,E501


# STRING module
# robotmesh.com/studio/content/docs/vexv5-python/html/namespacestring.html
# ========================================================================
from string import _Autobox, atoi, count, find, join, digits, hexdigits, letters  # noqa: E402,E501
