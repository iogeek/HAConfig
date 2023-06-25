#wiggle
msg = data.get("message")
if not msg:
    logger.error("esp-cmd:start:msg not passed in ")
    quit()
logger.info("esp-cmd:start:msg[%s]",msg)

haStateDict = {
    "on": "turn_on",
    "off": "turn_off"
}

#D3 D1 D2          mask   dec
# L  L  L   none    000   0
# L  H  L  Ctrl-1   001   1
# H  H  L  Ctrl-2   101   5
# L  L  H  Ctrl-4   010   2
# H  L  H  Ctrl-5   110   6
# L  H  H  Ctrl-6   011   3
# H  H  H  Ctrl-3   111   7
#
# // wemos d1 mini
#// d1=5, d2=4, d3=0,
#const char kOutputPin[] = {5, 4, 0}; 


sixChannelMask = {
  "0": "bit1:off,bit2:off,bit3:off",
  "1": "bit1:on,bit2:off,bit3:off",
  "2": "bit1:off,bit2:on,bit3:off",
  "3": "bit1:on,bit2:on,bit3:off",
  "4": "bit1:off,bit2:off,bit3:on",
  "5": "bit1:on,bit2:off,bit3:on",
  "6": "bit1:off,bit2:on,bit3:on",
  "7": "bit1:on,bit2:on,bit3:on"
}

ha6cUnitDict = {
    # Z1 units
    "z1_flower_path": "z1_main:3",
    "z1_berry_path": "z1_main:5",
    "z1_grid_drip": "z1_main:2",
    "z1_control_grid": "z1_main:6",
    "z1_control_beds": "z1_main:1",
    "z1_control_7": "z1_main:7",
    # Z2 units
    "z2-control-tub": "z2_main:2",
    "z2-control-yard-orchard": "z2_main:1",
    "z2-tulip-tree" : "z2_main:6",
    "z2-driveway" : "z2_main:7",
    "z2-control-5" : "z2_main:5",
    "z2-control-3" : "z2_main:3",
    # test units
    "test6c-1" : "test_6channel:1",
    "test6c-2" : "test_6channel:2",
    "test6c-3" : "test_6channel:3",
    "test6c-4" : "test_6channel:4",
    "test6c-5" : "test_6channel:5",
    "test6c-6" : "test_6channel:6"
}
# switch.test_6channel_bit1


haUnitDict = {
    # Z1 units
    "z1-grid1": "z1_grid12_sw1",
    "z1-grid2": "z1_grid12_sw2",
    "z1-grid3": "z1_grid34-sw1",
    "z1-grid4": "z1_grid34_sw2",
    "z1-grid5": "z1_grid56_sw1",
    "z1-grid6": "z1_grid56_sw2",
    "z1-grid7": "z1_grid78_sw1",
    "z1-grid8": "z1-grid78_sw2",
    "z1-grid9": "z1-grid90_sw1",
    "z1-grid10": "z1-grid90_sw2",
    "z1-bed1":  "z1-bed1-sw1",
    "z1-bed2": "z1-bed2-sw1",
    "z1-bed3": "z1-bed3-sw1",
    "z1-grape-wall": "z1-grape-wall-sw1",
    #z2 units
    "z2-rosemary": "z2_rosemary_sw1",
    "z2-bay-bush": "z2_bay_bush_sw1",
    "z2-grape": "z2_grape_sw1",
    "z2-big-pear":  "z2_big_pear_sw1",
    "z2-little-pear": "z2_little_pear_sw1",
    "z2-cherry" : "z2_cherry_apple_sw1",
    "z2-apple" : "z2_cherry_apple_sw2",
    "z2-tub1" : "z2_tub12_sw1",
    "z2-tub2" : "z2_tub12_sw2",
    "z2-tub3" : "z2_tub34_sw1",
    "z2-tub4" : "z2_tub34_sw2",
    "z2-tub5" : "z2_tub56_sw1",
    "z2-tub6" : "z2_tub56_sw2",
    "z2-tub7" : "z2_tub7_sw1",
    # test units
    "test1c" : "test_1_channel_sw1",
    "test2c-1" : "test_2channel_sw1",
    "test2c-2" : "test_2channel_sw2"
}

deviceStrList = msg.split(",")

for deviceStr in deviceStrList:
  logger.info("esp-cmd:deviceStr[%s]",deviceStr)
  deviceInfo = deviceStr.split(":")
  device = deviceInfo[0]
  state = haStateDict[deviceInfo[1]]
  if device in haUnitDict:
    device = "switch." + haUnitDict[device]
    logger.info("esp-cmd:1c/2c:name[%s]", device)
    entity = hass.states.get(device)
    if entity is None:
      logger.error("**Cannot find 1c/2c:name[%s].  Skipping it.", device)
    else:
      hass.services.call('homeassistant', state, {'entity_id': device})
  elif device in ha6cUnitDict:
    newSixChannelDeviceStr = ha6cUnitDict[device]
    newSixChannelDeviceInfo = newSixChannelDeviceStr.split(":")
    deviceSixChannel = newSixChannelDeviceInfo[0]
    bitMaskSixChannel = "0"
    # Get a proper bitmask iff a FET is to be enabled
    if state == "turn_on":
      bitMaskSixChannel = newSixChannelDeviceInfo[1]
    patternStr = sixChannelMask[bitMaskSixChannel]
    patternList = patternStr.split(",")
    for pattern in patternList:
      aPatternArray = pattern.split(":")
      #switch.z1_main_bit1
      device = "switch." + deviceSixChannel + "_" + aPatternArray[0]
      state = haStateDict[aPatternArray[1]]
      logger.info("esp-cmd:6c:name[%s]:state[%s]",device, state)
      entity = hass.states.get(device)
      if entity is None:
        logger.error("**Cannot find 6c:name[%s].  Skipping it.", device)
      else:
        hass.services.call('homeassistant', state, {'entity_id': device})
  else:
    logger.error("esp-cmd:unit[%s] not known from [%s] in msg[%s]", device, deviceStr, msg)
    quit()

logger.info("esp-cmd:end")


# switch.test_1_channel_sw1

# service_data = {'entity_id': 'input_boolean.toggle_flurlicht', 'state': state}
# hass.services.call("input_boolean", "turn_on", service_data, False)

# service_data = {'topic': 'python/sonoff/cmnd/error', 'payload': '{}'.format(state)}	
# hass.services.call("mqtt","publish",service_data, False)

# service_data = {"entity_id": entity_id, "rgb_color": rgb_color, "brightness": 255}
# hass.services.call("light", "turn_on", service_data, False)

#hass.services.call(‘media_player.squeezebox_call_method’, { “entity_id”: “media_player.squeezebox_radio”, “command”: “alarm”, “parameters”: [“update”, “id:582c05af”, “time:24000”] })
#hass.services.call(‘light’, action, service_data={ ‘entity_id’: ‘light.bathroom’, ‘state’: ‘on’, ‘brightness’: ‘255’, ‘kelvin’: ‘2700’ })