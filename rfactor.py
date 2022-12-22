from ctypes import LittleEndianStructure, c_int, c_float, c_double, c_char, c_byte, c_ubyte, c_bool, c_short, c_long, Array, wintypes

class RFVec3(LittleEndianStructure):
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
    ]

class RFWheel(LittleEndianStructure):
    _fields_ = [
        ('rotation', c_float),
        ('suspensionDeflection', c_float),
        ('rideHeight', c_float),
        ('tireLoad', c_float),
        ('lateralForce', c_float),
        ('gripFract', c_float),
        ('brakeTemp', c_float),
        ('pressure', c_float),
        ('temperature', c_float*3),
        ('wear', c_float),
        ('terrainName', c_char*16),
        ('surfaceType', c_ubyte),
        ('flat', c_bool),
        ('detached', c_bool),
    ]

# scoring info only updates twice per second (values interpolated when deltaTime > 0)!
class RFVehicleInfo(LittleEndianStructure):
    _fields_ = [
        ('driverName', c_char*32),
        ('totalLaps', c_short),
        ('sector', c_char),
        ('finishStatus', c_char),
        ('lapDist', c_float),
        ('pathLateral', c_float),
        ('trackEdge', c_float),

        ('bestSector1', c_float),
        ('bestSector2', c_float),
        ('bestLapTime', c_float),
        ('lastSector1', c_float),
        ('lastSector2', c_float),
        ('lastLapTime', c_float),
        ('curSector2', c_float),
        ('curSector2', c_float),

        ('numPitStops', c_short),
        ('numPenalties', c_short),
        ('isPlayer', c_bool),
        ('place', c_ubyte),
        ('vehicleClass', c_char*32),

        ('timeBehindNext', c_float),
        ('lapsBehindNext', c_long),
        ('timeBehindLeader', c_float),
        ('lapsBehindLeader', c_long),
        ('lapStartET', c_float),

        ('pos', RFVec3),

        ('yaw', c_float),
        ('pitch', c_float),
        ('roll', c_float),
        ('speed', c_float),
    ]

class RFShared(LittleEndianStructure):
    _fields_ = [
        ('version', c_char*8),
        ('deltaTime', c_float),
        ('lapNumber', c_long),
        ('lapStartET', c_float),
        ('trackName', c_char*64),
        ('pos', RFVec3),
        ('localVel', RFVec3),
        ('localAccel', RFVec3),
        ('oriX', RFVec3),
        ('oriY', RFVec3),
        ('oriZ', RFVec3),
        ('localRot', RFVec3),
        ('localRotAccel', RFVec3),
        ('speed', c_float),
        ('gear', c_long),
        ('engineRPM', c_float),
        ('engineWaterTemp', c_float),
        ('engineOilTemp', c_float),
        ('clutchRPM', c_float),
        ('unfilteredThrottle', c_float),
        ('unfilteredBrake', c_float),
        ('unfilteredSteering', c_float),
        ('unfilteredClutch', c_float),

        ('steeringArmForce', c_float),
        ('fuel', c_float),
        ('enggineMaxRPM', c_float),
        ('scheduledStops', c_ubyte),
        ('overheating', c_bool),
        ('detached', c_bool),
        ('dentSeverity', c_ubyte*8),
        ('lastImpactET', c_float),
        ('lastImpactMagnitude', c_float),
        ('lastImpactPos', RFVec3),
        ('rfWheel', RFWheel),
        ('session', c_long),
        ('currentET', c_float),
        ('endET', c_float),
        ('maxLaps', c_long),
        ('numVehicles', c_long),
        ('gamePhase', c_ubyte),
        ('yellowFlagState', c_char),
        ('sectorFlag', c_char*3),
        ('startLight', c_ubyte),
        ('numRedLights', c_ubyte),
        ('inRealTime', c_bool),
        ('playerName', c_char*32),
        ('ambientTemp', c_float),
        ('trackTemp', c_float),
        ('wind', RFVec3),
        ('vehicle', RFVehicleInfo*64),
    ]
