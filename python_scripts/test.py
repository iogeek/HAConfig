# this is just a script where i try stuff
def my_function():
  logger.info("Hello from a function")

my_function()

msg = data.get("message")
desiredState = data.get("state")  # on/off
desiredStations = data.get("stations") # all or station name (ie gh_station1)

if not msg:
    logger.error("test.py:start:msg not passed in ")
    #quit()  #not defined
logger.info("test.py:start:msg[%s]",msg)
logger.info("test.py:desiredStations[%s]:desiredState[%s]",desiredStations, desiredState)
