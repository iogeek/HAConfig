msg = ""
logger.info("on-boot:start:msg[%s]",msg)
hass.services.call('python_script', 'set_gh_stations', {'message': "name"})
#hass.services.call('homeassistant', state, {'entity_id': device})