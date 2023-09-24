# Helper script design to work with the "Test" card
# takes the input from the 2 text blocks to derive the
# python function to call and it parameters
parm1Str = data.get("parm1")
parm2Str = data.get("parm2")
parm3Str = data.get("parm3")
script = data.get("script")

if not script:
    logger.error("test_helper:script name not passed in: aborting ")
    #quit()
else:
    logger.info("test_helper:start:script[%s]:parm1[%s]:parm2[%s]",script,parm1Str,parm2Str)
    if not parm1Str:
        logger.info("test_helper:calling[%s]:no parms",script)
        hass.services.call('python_script', script, "")
    else:
        parm1List = parm1Str.split(":")
        if not parm2Str:
            logger.info("test_helper:calling[%s]:1 parm[%s]",script,parm1Str)
            hass.services.call('python_script', script, {parm1List[0]: parm1List[1]})
        else:
            parm2List = parm2Str.split(":")
            if not parm3Str:
                logger.info("test_helper:calling[%s]:2 parm[%s][%s]",script,parm1Str,parm2Str)
                hass.services.call('python_script', script, {parm1List[0]: parm1List[1], parm2List[0]: parm2List[1]})
            else:
                parm3List = parm3Str.split(":")
                logger.info("test_helper:calling[%s]:3 parm[%s][%s][%s]]",script,parm1Str,parm2Str, parm3Str)
                hass.services.call('python_script', script, {parm1List[0]: parm1List[1], parm2List[0]: parm2List[1], parm3List[0]: parm3List[1]})
 ## cannot use parmJSON += parmJSON
 ## cannot use eval

# parmList = parmStr.split(",")
# parmJSON = ""
# for parm in parmList:
#     logger.info("test_helper:parm[%s]",parm)
#     aList = parmStr.split(":")
#     aLen = len(aList)
#     pLen = len(parmJSON)
#     logger.info("test_helper:len(,)[%s]:len(:)[%s]",pLen,aLen)
#     if len(parmJSON) >= 1:
#         parmJSON += ","
#     varName = aList[0]
#     varValue = aList[1]
#     logger.info("test_helper:varName[%s]:varValue[%s]",varName,varValue)
#     parmJSON = parmJSON + '\'' + varName + '\':\'' + varValue +'\''  ## cannot use parmJSON += parmJSON
# parmJSON = "{" + parmJSON + "}"
# scriptStr = '\'' + script + '\''
# logger.info("test_helper:scriptStr[%s]:parmJSON[%s]",scriptStr,parmJSON)

#hass.services.call('python_script', script, eval(parmJSON))  ## cannot use eval
#hass.services.call('python_script', script, {'message': 'foo'})
#hass.services.call('python_script', 'set_gh_stations', {'message': "name"})
