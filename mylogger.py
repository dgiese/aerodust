import logging 
import datetime
import os

def config_logs():
    # Logfile
    logfolder = "logs/"
    logdate = datetime.datetime.now().strftime("%y-%m-%d_%H:%M") + "_"
    logfile = "aerodust.log"

    logpath = logfolder + logfile
    #logpath = logfolder + logdate + logfile
    if not os.path.exists(logfolder):
            os.makedirs(logfolder)

    # Format
    logformat = '%(asctime)s %(levelname)s: %(message)s'
    datefmt='%m/%d/%Y %I:%M:%S %p'

    # Get the Root Logger and
    rootLogger = logging.getLogger()

    # Create a formatter
    logFormatter = logging.Formatter(logformat, datefmt)

    # Create and add the file stream handler to the logger
    fileHandler = logging.FileHandler(logpath)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    # Create and add the console stream handler to the logger
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    rootLogger.setLevel(logging.INFO)
    #rootLogger.setLevel(logging.DEBUG)
