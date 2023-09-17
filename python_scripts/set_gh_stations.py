desiredState = data.get("state")  # on/off
desiredStations = data.get("stations") # all or station name (ie gh_station1)
logger.info("set_gh_stattions:start:desiredStations[%s]:desiredState[%s]",desiredStations, desiredState)

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

dataTable = [
# toggle switch      light list           heat list
 #["test",           "test.test",          "test.test"], 
  ["gh_station0",    "switch.sw6p4",       "switch.sw1p1"], 
  ["gh_station1",    "switch.sw6p2",       "switch.sw6p1"], 
  ["gh_station2",    "switch.sw1p2",       "switch.sw1p3"],
  ["gh_station3",    "switch.sw6p6",       "switch.sw5p3"],  
  ["gh_station4",    "switch.sw4p1",       "switch.sw4p2,switch.sw4p3,switch.sw4p4"], #
  ["gh_station5",    "switch.sw5p1",       "switch.sw3p5"],  
  ["gh_station6",    "switch.sw3p1",       "switch.sw3p3"],  
  ["gh_station7",    "switch.sw5p2",       "switch.sw3p4"],
  ["gh_station8",    "switch.sw5p1",       "switch.sw3p6"],
  ["gh_station9",    "switch.sw3p1",       "switch.sw4p5"],
  ["gh_station10",   "switch.sw5p2",       "switch.sw4p6"],
  ["gh_station11",   "switch.sw2p2",       "switch.sw2p3"]
]


sharedTable = {
  "gh_station5":    ["gh_station8:light"],
  "gh_station6":    ["gh_station9:light"],  
  "gh_station7":    ["gh_station10:light"],
  "gh_station8":    ["gh_station5:light"],
  "gh_station9":    ["gh_station6:light"],
  "gh_station10":   ["gh_station7:light"],
}

##############################################
#  Functions
##############################################
def setEntityState(station, eId, state, bIsSingle):
  logger.info("set_gh_stations:setEntityState")
  if station in sharedTable:
    logger.info("set_gh_stations:setEntityState:station[%s] found in sharedTable", station)
  else:
    logger.info("set_gh_stations:setEntityState:station[%s] is not shared", station)

##############################################
#  main
##############################################



# All, enabled
# on/off
newLightState = "off"
newHeatState = "off"
doLight = True
doHeat = True
if desiredStations == "all":
  for itmList in dataTable:
    itm = itmList[0]
    lightName = itmList[1]
    heatName = itmList[2]
    eName = "input_boolean." + itm
    eId = hass.states.get(eName)
    if eId is  None:
      logger.error("**set_gh_stations:Cannot find name[%s].  skipping", eName)
      continue
    inUse = eId.state
    #setEntityState()
    logger.info("set_gh_stations:entitiy[%s] inUse [%s]", eName, inUse)
    setEntityState(desiredStations, desiredState, True)
else:
  eName = "input_boolean." + desiredStations
  eId = hass.states.get(eName)
  if eId is  None:
    logger.error("**set_gh_stations:Cannot find name[%s].  skipping", eName)
  inUse = eId.state
  logger.info("set_gh_stations:calling setEntityState:entitiy[%s] inUse [%s]", eName, inUse)
  setEntityState(desiredStations, desiredState, False)


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