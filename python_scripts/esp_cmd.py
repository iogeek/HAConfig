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

sixChannelMask = {
  "0": "bit1:off,bit2:off,bit3:off",
  "1": "bit1:on,bit2:off,bit3:off",
  "2": "bit1:off,bit2:on,bit3:off",
  "3": "bit1:on,bit2:on,bit3:off",
  "4": "bit1:off,bit2:off,bit3:on",
  "5": "bit1:on,bit2:off,bit3:on",
  "6": "bit1:off,bit2:on,bit3:on"
}

ha6cUnitDict = {
    # Z1 units
    "z1_flower_path": "z1_main:3",
    "z1_berry_path": "z1_main:5",
    "z1_grid_drip": "z1_main:2",
    "z1_control_grid": "z1_main:6",
    "z1_control_beds": "z1_main:1",
    "z1_control_4": "z1_main:4",
    # Z2 units
    "z2-control-tub": "z2-main:1",
    "z2-control-yard-orchard": "z2-main:2",
    "z2-tulip-tree" : "z2-main:3",
    "z2-front-flowerbed" : "z2-main:4",
    "z2-control-5" : "z2-main:5",
    "z2-control-6" : "z2-main:6",
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
    "z1-grid4": "z1_grid34-sw2",
    "z1-grid5": "z1_grid56-sw1",
    "z1-grid6": "z1_grid56-sw2",
    "z1-grid7": "z1_grid78-sw1",
    "z1-grid8": "z1-grid78-sw2",
    "z1-grid9": "z1-grid90-sw1",
    "z1-grid10": "z1-grid90-sw2",
    "z1-bed1":  "z1-bed1-sw1",
    "z1-bed2": "z1-bed2-sw1",
    "z1-bed3": "z1-bed3-sw1",
    "z1-grape-wall": "z1-grape-wall-sw1",
    #z2 units
    "z2-rosemary": "z2-rosemary-sw1",
    "z2-bay-bush": "z2-bay-bush-sw1",
    "z2-grape": "z2-grape-sw1",
    "z2-big-pear":  "z2-big-pear-sw1",
    "z2-little-pear": "z2-little-pear-sw1",
    "z2-cherry" : "z2-cherry-apple-sw1",
    "z2-apple" : "z2-cherry-apple-sw2",
    "z2-tub1" : "z2-tub12-sw1",
    "z2-tub2" : "z2-tub12-sw2",
    "z2-tub3" : "z2-tub34-sw1",
    "z2-tub4" : "z2-tub34-sw2",
    "z2-tub5" : "z2-tub56-sw1",
    "z2-tub6" : "z2-tub56-sw2",
    "z2-tub7" : "z2-tub7-sw1",
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