from ctypes import LittleEndianStructure, c_int, c_float, Array, wintypes
from enum import IntEnum

from .rfactor2 import RF2Telemetry
from .ac import SPageFilePhysics, SPageFileGraphic, SPageFileStatic

class SimAPI(LittleEndianStructure):
    _fields_ = [
        ('velocity', c_int),
        ('rpms', c_int),
        ('gear', c_int),
        ('pulses', c_int),
        ('maxrpm', c_int),
        ('altitude', c_int),
        ('lap', c_int),
    ]

types = {
    'acpmf_physics': SPageFilePhysics,
    'acpmf_graphics': SPageFileGraphic,
    #'acpmf_static': SPageFileStatic,
    
    'rFactor2SMMP_Telemetry': RF2Telemetry,

    'simapi_test': SimAPI,
}
