#wiggle
msg = data.get("message")
if not msg:
    logger.info("esp-cmd msg not passed in ")
    quit()
logger.info("esp-cmd unit_state msg[%s]",msg)

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
    "z1_flower_path": "z1_main:1",
    "z1_berry_path": "z1_main:2",
    "z1_grid_drip": "z1_main:3",
    "z1_control_grid": "z1_main:4",
    # Z2 units
    "z2_control_tub": "z2_main:1",
    "z2_control_yard_orchard": "z2_main:2",
    "z2_tulip_tree" : "z2_main:3",
    "z2_front_flowerbed" : "z2_main:4"
}


haUnitDict = {
    # Z1 units
    "z1_grid1": "z1_grid12_sw1",
    "z1_grid2": "z1_grid12_sw2",
    "z1_grid3": "z1_grid34_sw1",
    "z1_grid4": "z1_grid34_sw2",
    "z1_grid5": "z1_grid56_sw1",
    "z1_grid6": "z1_grid56_sw2",
    "z1_grid7": "z1_grid78_sw1",
    "z1_grid8": "z1_grid78_sw2",
    "z1_grid9": "z1_grid90_sw1",
    "z1_grid10": "z1_grid90_sw2",
    "z1_bed1":  "z1_bed1_sw1",
    "z1_bed2": "z1_bed2_sw1",
    "z1_bed3": "z1_bed3_sw1",
    "z1_grape_wall": "z1_grape_wall_sw1",
    #z2 units
    "z2_rosemary": "z2_rosemary_sw1",
    "z2_bay_bush": "z2_bay_bush_sw1",
    "z2_grape": "z2_grape_sw1",
    "z2_big_pear":  "z2_big_pear_sw1",
    "z2_little_pear": "z2_little_pear_sw1",
    "z2_cherry" : "z2_cherry_apple_sw1",
    "z2_apple" : "z2_cherry_apple_sw2",
    "z2_tub1" : "z2_tub12_sw1",
    "z2_tub2" : "z2_tub12_sw2",
    "z2_tub3" : "z2_tub34_sw1",
    "z2_tub4" : "z2_tub34_sw2",
    "z2_tub5" : "z2_tub56_sw1",
    "z2_tub6" : "z2_tub56_sw2",
    "z2_tub7" : "z2_tub7_sw1"
}

deviceStrList = msg.split(",")

for deviceStr in deviceStrList:
  deviceInfo = deviceStr.split(":")
  device = deviceInfo[0]
  state = haStateDict[deviceInfo[1]]
  print f

# switch.test_1_channel_sw1