#wiggle
msg = data.get("message")
if not msg:
    logger.info("esp-cmd msg not passed in ")
logger.info("esp-cmd unit_state msg[%s]",msg)