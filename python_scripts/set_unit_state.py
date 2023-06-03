
msg = data.get("message")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

sixChannelArray = ["Ford", "Volvo", "BMW"]

sixChannelMask = {
  "0": "bit1:off,bit2:off,bit3:off",
  "1": "bit1:on,bit2:off,bit3:off",
  "2": "bit1:off,bit2:on,bit3:off",
  "3": "bit1:on,bit2:on,bit3:off",
  "4": "bit1:off,bit2:off,bit3:on",
  "5": "bit1:on,bit2:off,bit3:on",
  "6": "bit1:off,bit2:on,bit3:on"
}


logger.info("set_unit_state state[%s] name[%s]",msg)
#if state == "off":
#    hass.services.call('homeassistant', 'turn_off', {'entity_id': name})
#    logger.info("set_unit_state turned off")
#else:
#    hass.services.call('homeassistant', 'turn_on', {'entity_id': name})
#    logger.info("set_unit_state turned on")
logger.info("set_unit_state done")