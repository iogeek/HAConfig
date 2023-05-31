state = data.get("state")
name = data.get("name")


logger.info("set_unit_state state[%s] name[%s]",state, name)
if state == "off":
    hass.services.call('homeassistant', 'turn_off', {'entity_id': name})
    logger.info("set_unit_state turned off")
else:
    hass.services.call('homeassistant', 'turn_on', {'entity_id': name})
    logger.info("set_unit_state turned on")
logger.info("set_unit_state done")