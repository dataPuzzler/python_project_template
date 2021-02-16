def toggle_debug():
    global DEBUG
    logger.debug("Switch 'DEBUG' Mode from %s to %s" % (str(DEBUG), str(not DEBUG)))
    DEBUG = not DEBUG


toggle_debug()
toggle_debug()