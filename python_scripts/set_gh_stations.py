msg = ""
logger.info("set_gh_stattions:start:msg[%s]",msg)

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
  "gh_station5":    ["gh_station8",   "switch.sw5p1"],
  "gh_station6":    ["gh_station9",   "switch.sw3p1"],  
  "gh_station7":    ["gh_station10",  "switch.sw5p2"],
  "gh_station8":    ["gh_station5",   "switch.sw5p1"],
  "gh_station9":    ["gh_station6",   "switch.sw3p1"],
  "gh_station10":   ["gh_station7",   "switch.sw5p2"]
}

# All, enabled
# on/off

for itmList in dataTable:
  eName = "input_boolean." + itmList[0]
  eId = hass.states.get(eName)
  state = eId.state
  logger.info("entitiy[%s] is [%s]", eName, state)

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