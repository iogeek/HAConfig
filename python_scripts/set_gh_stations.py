desiredState = data.get("state")  # on/off
desiredStations = data.get("stations") # all or station name (ie gh_station1)
logger.info("set_gh_stations:start:desiredStations[%s]:desiredState[%s]",desiredStations, desiredState)

#light                                      heat
#                           sw 1
# #- switch.sw1p2 #s2                   #- switch.sw1p1 #s0
#                                       #- switch.sw1p3 #s2
#                          sw 2
# #- switch.sw2p2 #s11                  #- switch.sw2p3 #s11
#                          sw 3
# #- switch.sw3p1 #s6/9                 # - switch.sw3p3 #s6
#                                       # - switch.sw3p4 #s7
#                                       # - switch.sw3p5 #s5
#                                       # - switch.sw3p6 #s8
#                          sw 4
# #- switch.sw4p1 #s4                   # - switch.sw4p2 #s4-1
#                                       # - switch.sw4p3 #s4-2
#                                       # - switch.sw4p4 #s4-3
#                                       # - switch.sw4p5 #s9
#                                       # - switch.sw4p6 #s10
#                          sw 5
# #- switch.sw5p1 #s5/8                 #- switch.sw5p3 #s3
# #- switch.sw5p2 #s7/10
#                          sw 6
# #- switch.sw6p2 #s1                   #- switch.sw6p1 #s1
# #- switch.sw6p4 #s0
# #- switch.sw6p6 #s3

lightData = {
# toggle switch      light list    
 #["test",           "test.test",  
  "gh_station0":    "switch.sw6p4",
  "gh_station1":    "switch.sw6p2",
  "gh_station2":    "switch.sw1p2",
  "gh_station3":    "switch.sw6p6",
  "gh_station4":    "switch.sw4p1",
  "gh_station5":    "switch.sw5p1",
  "gh_station6":    "switch.sw3p1",
  "gh_station7":    "switch.sw5p2",
  "gh_station8":    "switch.sw5p1",
  "gh_station9":    "switch.sw3p1",
  "gh_station10":   "switch.sw5p2",
  "gh_station11":   "switch.sw2p2",
}


heatData = {
# toggle switch      heat list
 #["test",            "test.test"], 
  "gh_station0":     "switch.sw1p1", 
  "gh_station1":     "switch.sw6p1", 
  "gh_station2":     "switch.sw1p3",
  "gh_station3":     "switch.sw5p3",  
  "gh_station4":     "switch.sw4p2,switch.sw4p3,switch.sw4p4", #
  "gh_station5":     "switch.sw3p5",  
  "gh_station6":     "switch.sw3p3",  
  "gh_station7":     "switch.sw3p4",
  "gh_station8":     "switch.sw3p6",
  "gh_station9":     "switch.sw4p5",
  "gh_station10":    "switch.sw4p6",
  "gh_station11":    "switch.sw2p3"
}


sharedLight = {
  "gh_station5":    "gh_station8",
  "gh_station6":    "gh_station9",  
  "gh_station7":    "gh_station10",
  "gh_station8":    "gh_station5",
  "gh_station9":    "gh_station6",
  "gh_station10":   "gh_station7"
}

sharedHeat = {
}

##############################################
#  Functions
##############################################
def setStationState(station, state):
  logger.info("set_gh_stations:setEntityState:station[%s]:state[%s]", station, state)
  if station in sharedDict:
    logger.info("set_gh_stations:setEntityState:station[%s] found in sharedTable", station)
    if state == "off":
      logger.info("set_gh_stations:setEntityState:station[%s] is shared and off", station)

  else:
    logger.info("set_gh_stations:setEntityState:station[%s] is not shared", station)
    hass.services.call('homeassistant', state, {'entity_id': device})

def setStationLight(station, state):
  if station in sharedLight:
    logger.info("set_gh_stations:setStation:station[%s] is sharedLight", station)

def setStationHeat(station, state):
  if station in sharedHeat:
    logger.info("set_gh_stations:setStationHeat:station[%s] is sharedHeat", station)
    # if shared station is disabled and we are turning off then proceed
    # if shared station is disabled and we are turning on then proceed
    # if shared station is enabled and we changed to shared stations state then proceed
    # if shared station is enabled and new state differs then do nothing
  else:
    stationStr = heatData[station]
    stationList = stationStr.split(",")
    for id in stationList:
      logger.info("set_gh_stations:setStationHeat:id[%s] to [%s]", id, state)
      hass.services.call('homeassistant', state, {'entity_id': id})

def getStationBias(station, sharedStationTable, stationTypeTable, state):
  if station in sharedStationTable:
    logger.info("set_gh_stations:setStationHeat:station[%s] is sharedHeat", station)
    # if shared station is disabled and we are turning off then proceed
    # if shared station is disabled and we are turning on then proceed
    # if shared station is enabled and we changed to shared stations state then proceed
    # if shared station is enabled and new state differs then do nothing
  else:
    return False     # not shared.  So no bias
  return False       # should never get here.

def setStation(station, state, bUseBias):
  # set both heat and light
  logger.info("set_gh_stations:setStation:station[%s]:state[%s]:bias[%s]", station, state, bUseBias)
  # setStationLight(station, state)
  # setStationHeat(station, state)



##############################################
#  main
##############################################
if desiredStations == "all":
else:
  station = desiredStations.split(".")  # will be in the format of 'input_boolean.gh_station1'
  setStation(station[1], desiredState, True)




# All, enabled
# on/off
# newLightState = "off"
# newHeatState = "off"
# doLight = True
# doHeat = True
# if desiredStations == "all":
#   for itmList in dataTable:
#     itm = itmList[0]
#     lightName = itmList[1]
#     heatName = itmList[2]
#     eName = "input_boolean." + itm
#     eId = hass.states.get(eName)
#     if eId is  None:
#       logger.error("**set_gh_stations:Cannot find name[%s].  skipping", eName)
#       continue
#     inUse = eId.state
#     #setEntityState()
#     logger.info("set_gh_stations:entitiy[%s] inUse [%s]", eName, inUse)
#     setEntityState(desiredStations, desiredState, True)
# else:
#   eName = "input_boolean." + desiredStations
#   eId = hass.states.get(eName)
#   if eId is  None:
#     logger.error("**set_gh_stations:Cannot find name[%s].  skipping", eName)
#   inUse = eId.state
#   logger.info("set_gh_stations:calling setEntityState:entitiy[%s] inUse [%s]", eName, inUse)
#   setEntityState(desiredStations, desiredState, False)


  #if inUse == "on":
  #  if desiredState == "on":
  #    newState = "on"
  # assume desiredState should be off for anything else
  #logger.info("entitiy[%s] newState [%s]", eName, newState)

# changing all states
# if itm is shared, then
#   if shred_itm inUse then set to new state
#   else set to new state

 # if itm in sharedTable:
 #   sharedItmList = sharedTable[itm]





#logger.error("**Cannot find 1c/2c:name[%s].  Skipping it.", device)
# state = hass.states.get(entity_id)
# if state.state == 'on':


#    device = "switch." + deviceSixChannel + "_" + aPatternArray[0]
#   state = haStateDict[aPatternArray[1]]
#   logger.debug("esp-cmd:6c:name[%s]:state[%s]",device, state)
#   entity = hass.states.get(device)
#   if entity is None:
#     logger.error("**Cannot find 6c:name[%s].  Skipping it.", device)
#   else:
#     hass.services.call('homeassistant', state, {'entity_id': device})