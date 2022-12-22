from ctypes import LittleEndianStructure, c_int, c_float, c_double, c_char, c_byte, c_ubyte, c_bool, c_short, c_long, Array, wintypes

class RF2Vec3(LittleEndianStructure):
    
    _pack_ = 4
    _fields_ = [
        ('x', c_double),
        ('y', c_double),
        ('z', c_double),
    ]

class RF2Wheel(LittleEndianStructure):
    
    _pack_ = 4
    _fields_ = [
        ('mSuspensionDeflection', c_double),
        ('mRideHeight', c_double),
        ('mSuspForce', c_double),
        ('mBrakeTemp', c_double),
        ('mBrakePressure', c_double),

        ('mRotation', c_double),
        ('mLateralPatchVel', c_double),
        ('mLongitudinalPatchVel', c_double),
        ('mLateralGroundVel', c_double),
        ('mLongitudinalGroundVel', c_double),
        ('mCamber', c_double),
        ('mLateralForce', c_double),
        ('mLongitudinalForce', c_double),
        ('mTireLoad', c_double),
        
        ('mGripFract', c_double),
        ('mPressure', c_double),
        ('mTemperature', c_double*3),
        ('mWear', c_double),
        
        ('mTerrainName', c_byte*16),
        ('mSurfaceType', c_ubyte),
        ('mFlat', c_bool),
        ('mDetached', c_bool),
        
        ('mStaticUndeflectedRadius', c_ubyte),
        ('mVerticalTireDeflection', c_double),
        ('mWheelYLocation', c_double),
        ('mToe', c_double),
        ('mTireCarcassTemperature', c_double),
        ('mTireInnerLayerTemperature', c_double*3),
        
        ('mExpansion', c_ubyte*24),
    ]

class RF2VehicleTelemetry(LittleEndianStructure):
    _pack_ = 4
    _fields_ = [
        ('mID', c_int),
        ('mDeltaTime', c_double),
        ('mElapsedTime', c_double),
        ('mLapNumber', c_int),
        ('mLapStartET', c_double),
        ('mVehicleName', c_char*64),
        ('mTrackName', c_char*64),

        ('mPos', RF2Vec3),
        ('mLocalVel', RF2Vec3),
        ('mLocalAccel', RF2Vec3),
        ('mOri', RF2Vec3*3),
        ('mLocalRot', RF2Vec3),
        ('mLocalRotAccel', RF2Vec3),
        
        ('mGear', c_int),
        ('mEngineRPM', c_double),
        ('mEngineWaterTemp', c_double),
        ('mEngineOilTemp', c_double),
        ('mClutchRPM', c_double),

        ('mUnfilteredThrottle', c_double),
        ('mUnfilteredBrake', c_double),
        ('mUnfilteredSteering', c_double),
        ('mUnfilteredClutch', c_double),

        ('mFilteredThrottle', c_double),
        ('mFilteredBrake', c_double),
        ('mFilteredSteering', c_double),
        ('mFilteredClutch', c_double),

        ('mSteeringShaftTorque', c_double),
        ('mFrontt3rdDeflection', c_double),
        ('mRear3rdDeflection', c_double),

        ('mFrontWingHeight', c_double),
        ('mFrontRideHeight', c_double),
        ('mRearRideHeight', c_double),
        ('mDrag', c_double),
        ('mFrontDownforce', c_double),
        ('mRearDownforce', c_double),

        ('mFuel', c_double),
        ('mEngineMaxRPM', c_double),
        ('mScheduledStops', c_ubyte),
        ('mOverheating', c_bool),
        ('mDetached', c_bool),
        ('mHeadlights', c_bool),
        
        ('mDentSeverity', c_ubyte*8),
        ('mLastImpactET', c_double),
        ('mLastImpactMagnitude', c_double),
        ('mLastImpactPos', RF2Vec3),

        ('mEngineTorque', c_double),
        ('mCurrentSector', c_int),
        ('mSpeedLimiter', c_ubyte),
        ('mMaxGears', c_ubyte),
        ('mFrontTireCompoundIndex', c_ubyte),
        ('mRearTireCompoundIndex', c_ubyte),
        ('mFuelCapacity', c_double),
        ('mFrontFlapActivated', c_ubyte),
        ('mRearFlapActivated', c_ubyte),
        ('mRearFlapLegalStatus', c_ubyte),
        ('mIgnitionStarter', c_ubyte),

        ('mFrontTireCompound', c_byte*18),
        ('mRearTireCompound', c_byte*18),
        
        ('mSpeedLimiterAvailable', c_ubyte),
        ('mAntiStallActivated', c_ubyte),
        ('mUnused', c_ubyte*2),
        ('mVisualSteeringWheelRange', c_float),

        ('mRearBrakeBias', c_double),
        ('mTurboBoostPressure', c_double),
        ('mPhysicToGraphicsOffset', c_float*3),
        ('mPhysicalSteeringWheelRange', c_float),

        ('mExpansion', c_ubyte*152),
        ('mWheels', RF2Wheel*4),

    ]


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

        ('pos', RF2Vec3),

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
        ('pos', RF2Vec3),
        ('localVel', RF2Vec3),
        ('localAccel', RF2Vec3),
        ('oriX', RF2Vec3),
        ('oriY', RF2Vec3),
        ('oriZ', RF2Vec3),
        ('localRot', RF2Vec3),
        ('localRotAccel', RF2Vec3),
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
        ('lastImpactPos', RF2Vec3),
        ('rfWheel', RF2Wheel),
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
        ('wind', RF2Vec3),
        ('vehicle', RFVehicleInfo*64),
    ]


class RF2Telemetry(LittleEndianStructure):

    _pack_ = 4
    _fields_ = [
        ('mVersionUpdateBegin', c_int),
        ('mVersionUpdateEnd', c_int),
        ('mBytesUpdatedHint', c_int),
        ('mNumVehicles', c_int),

        ('mVehicles', RF2VehicleTelemetry*64),
    ]
