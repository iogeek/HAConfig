desiredState = data.get("state")  # on/off
desiredStations = data.get("stations") # all or station name (ie gh_station1)
logger.info("set_gh_stations:start:desiredStations[%s]:desiredState[%s]",desiredStations, desiredState)


lightData = {
# toggle switch      light list    
 #["test",           "test.test",  
  "gh_station0":    "group.gh_station_light_0",
  "gh_station1":    "group.gh_station_light_1",
  "gh_station2":    "group.gh_station_light_2",
  "gh_station3":    "group.gh_station_light_3",
  "gh_station4":    "group.gh_station_light_4",
  "gh_station5":    "group.gh_station_light_5",
  "gh_station6":    "group.gh_station_light_6",
  "gh_station7":    "group.gh_station_light_7",
  "gh_station8":    "group.gh_station_light_8"
}


heatData = {
# toggle switch      heat list
 #["test",            "test.test"], 
  "gh_station0":     "group.gh_station_heat_0", 
  "gh_station1":     "group.gh_station_heat_1", 
  "gh_station2":     "group.gh_station_heat_2",
  "gh_station3":     "group.gh_station_heat_3",  
  "gh_station4":     "group.gh_station_heat_4", #
  "gh_station5":     "group.gh_station_heat_5",  
  "gh_station6":     "group.gh_station_heat_6",  
  "gh_station7":     "group.gh_station_heat_7",
  "gh_station8":     "group.gh_station_heat_8"
}


sharedLight = {
 # "gh_station5":    "gh_station8",
 # "gh_station6":    "gh_station9",  
 # "gh_station7":    "gh_station10",
 # "gh_station8":    "gh_station5",
 # "gh_station9":    "gh_station6",
 # "gh_station10":   "gh_station7"
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


def setState(idStr, state):
  logger.info("set_gh_stations:setState:idStr[%s] to [%s]", idStr, state)
  idList = idStr.split(",")
  for id in idList:
    logger.info("set_gh_stations:setState:id[%s] to [%s]", id, state)
    haState = "turn_off"
    if state == "on":
      haState = "turn_on"
    hass.services.call('homeassistant', haState, {'entity_id': id})

def getStationBias(station, sharedStationTable, stationTypeTable, state):
  logger.info("set_gh_stations:setStationHeat:start:station[%s]:state[%s]", station,state)
  if station in sharedStationTable:
    logger.info("set_gh_stations:setStationHeat:station[%s] is shared", station)
    sharedStation = sharedStationTable[station]
    sharedStationID = "input_boolean." + sharedStation
    sharedStationEnabledState =  hass.states.get(sharedStationID).state
    logger.info("set_gh_stations:setStationHeat:sharedtation[%s]:sharedStationState[%s]", sharedStation, sharedStationEnabledState)
    # if shared and primary station are disabled then turn off 
    # if shared station is disabled and we are turning on then proceed  # if disabled then state should not matter
    if sharedStationEnabledState == "off":   # if sharedStation is disabled then we can set any state.
      return False
    else:
      # if shared station is enabled and we changed to shared stations state then proceed
      # if shared station is enabled and new state differs then do nothing
      return True
  else:
    return False     # not shared.  So no bias
  return True       # should never get here.

def setStationState(station, state, sharedTable, table, bForce):
  idStr = table[station]
  if bForce == True:
    setState(idStr, state)
  else:
    if getStationBias(station, sharedTable, table, state) == False:
      logger.info("set_gh_stations:setStationState:station[%s].  No bias.  Proceed with setting state [%s]", station, state)
      setState(idStr, state)
    else:
      logger.info("set_gh_stations:setStationState:station[%s]. Has bias.  No state change. [%s]", station)
    


def setStation(station, state, bForce):
  # set both heat and light
  logger.info("set_gh_stations:setStation:station[%s]:state[%s]:force set[%s]", station, state, bForce)
  logger.info("set_gh_stations:setStation:-------- light ------")
  setStationState(station, state, sharedLight, lightData, bForce)
  logger.info("set_gh_stations:setStation:-------- heat ------")
  setStationState(station, state, sharedHeat, heatData, bForce)



##############################################
#  main
##############################################
if desiredStations == "all":
  for key in lightData:   # assume there was lightData and heatData have same stations
    stationToggle = "input_boolean." + key
    enabledState =  hass.states.get(stationToggle).state
    if enabledState == "on":
      setStation(key, desiredState, True)
else:
  station = desiredStations.split(".")  # will be in the format of 'input_boolean.gh_station1'
  setStation(station[1], desiredState, False)

hass.services.call('python_script', 'set_gh_groups', {})
logger.info("set_gh_stations:end:")


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