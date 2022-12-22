from ctypes import LittleEndianStructure, c_int, c_int16, c_float, c_char, c_byte, c_ubyte, c_bool, c_short, c_long, Array, wintypes
from enum import IntEnum

class SPageFilePhysics(LittleEndianStructure):
    _fields_ = [
        ('packetId', c_int),
        ('gas', c_float),
        ('brake', c_float),
        ('fuel', c_float),
        ('gear', c_int),
        ('rpms', c_int),
        ('steerAngle', c_float),
        ('speedKmh', c_float),
        ('velocity', c_float*3),
        ('accG', c_float*3),
        ('wheelSlip', c_float*4),
        ('wheelsPressure', c_float*4),
        ('tyreWear', c_float*4),
        ('tyreDirtyLevel', c_float*4),
        ('tyreCoreTemperature', c_float*4),
        ('camberRAD', c_float*4),
        ('suspensionTravel', c_float*4),
        ('drs', c_float),
        ('tc', c_float),
        ('heading', c_float),
        ('pitch', c_float),
        ('roll', c_float),
        ('cgHeight', c_float),
        ('carDamage', c_float*5),
        ('numberOfTyresOut', c_int),
        ('pitLimiterOn', c_int),
        ('abs', c_float),
    ]

class SPageFileGraphic(LittleEndianStructure):
    _fields_ = [
        ('packetId', c_int),
        ('acStatus', c_int),
        ('acSessionType', c_int),
        ('currentTime', c_int16*15),
        ('lastTime', c_int16*15),
        ('bestTime', c_int16*15),
        ('split', c_int16*15),

        ('completedLaps', c_int),
        ('position', c_int),
        ('iCurrentTime', c_int),
        ('iLastTime', c_int),
        ('iBestTime', c_int),
        ('sessionTimeLeft', c_float),
        ('distanceTraveled', c_float),
        ('isInPit', c_int),
        ('currentSectorIndex', c_int),
        ('lastSectorTime', c_int),
        ('numberOfLaps', c_int),
        ('tyreCompound', c_char*33),

        ('replayTimeMultiplier', c_float),
        ('normalizedCarPosition', c_float),
        ('carCoordinates', c_float*3),
    ]

class SPageFileStatic(LittleEndianStructure):
    _fields_ = [
        ('smVersion', c_char*15),
        ('acVersion', c_char*15),
        ('numberOfSessions', c_int),
        ('numCars', c_int),
        ('carModel', c_char*33),
        ('track', c_char*33),
        ('playerName', c_char*33),
        ('playerSurname', c_char*33),
        ('playerNick', c_char*33),
        ('sectorCount', c_int),

        ('maxTorque', c_float),
        ('maxPower', c_float),
        ('maxRpm', c_int),
        ('maxFuel', c_float),
        ('suspesionMaxTravel', c_float*4),
        ('tyreRadius', c_float*4),

        ('maxTurboBoost', c_float),
        ('deprecated1', c_float),
        ('deprecated2', c_float),
        ('penaltiesEnabled', c_int),
        ('aidFuelRate', c_float),
        ('aidTireRate', c_float),
        ('aidMechanicalDamage', c_float),
        ('aidAllowTyreBlankets', c_int),
        ('aidStability', c_float),
        ('aidAutoClutch', c_int),
        ('aidAutoBlip', c_int),

        ('hasDRS', c_int),
        ('hasERS', c_int),
        ('hasKERS', c_int),
        ('kersMaxJoules', c_float),
        ('engineBrakeSettingsCount', c_int),
        ('ersPowerControllercount', c_int),
        ('trackSPlineLength', c_float),
        ('trachConfiguration', c_char*15),
        ('ersMaxJ', c_float),

        ('isTimedRace', c_int),
        ('hasExtraLap', c_int),
        ('carSkin', c_char*33),
        ('reversedGridPositions', c_int),
        ('pitWindowStart', c_int),
        ('pitWindowEnd', c_int),

    ]


