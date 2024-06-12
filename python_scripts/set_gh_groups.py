
logger.info("set_gh_groups:start")
# https://flemmingss.com/how-to-make-home-assistant-groups-dynamic-and-user-manageable-through-lovelace/#:~:text=Add%20one%20or%20more%20entity%20to%20a%20group%3A,service%3A%20group.set%20data%3A%20object_id%3A%20name_of_group%20add_entities%3A%20domain.entity_a%2C%20domain.entity_b

#   action: call-service
#   service: group.set
#   service_data:
#     object_id: test_group
#     add_entities: light.lamp_2

# service: group.set
# data:
#   object_id: name_of_group
#   add_entities: domain.entity_a, domain.entity_b

# hass.services.call('media_player', 'squeezebox_call_method', { “entity_id”: “media_player.squeezebox_radio”, “command”: “alarm”, “parameters”: [“update”, “id:582c05af”, “time:24000”] }, False)

# https://community.home-assistant.io/t/create-a-group-and-assign-entities-programmatically/235435/3

# =====================================================================================
# ================== Example: creating / deleting entities in a group ========================
# domain = data.get('domain')
# group = data.get('group')

# service_data = {"object_id": group, "entities": hass.states.entity_ids(domain)}
# hass.services.call("group", "set", service_data, False)

# =====================================================================================
# ========= example: reading entities in a group ======================================
# group = data.get('group')
# input_select = data.get('input_select')

# if group is not None and input_select is not None:
#     group_entities = hass.states.get(group).attributes['entity_id']
#     list = []
#     for e in group_entities:
#         list.append(e)
#     service_data = {'entity_id': input_select,
#                     'options': list}
#     hass.services.call('input_select', 'set_options', service_data)
# else:
#     logger.warning('Missing arguments!')

# groups
# gh_station_light_xx
# gh_station_heat_xx

# gh_station_xx
# gh_auto_heat_mats: / gh_enabled_heat_mats:

# input_boolean.gh_stationxx


service_data = {"object_id": "gh_auto_heat_mats", "entities": "group.gh_station_heat_7"}
hass.services.call("group", "set", service_data, False)
ibools = data.get('input_boolean')
for i in ibools:
    z = i.attributes['entity_id']
    logger.info(z)
logger.info("set_gh_groups:end")