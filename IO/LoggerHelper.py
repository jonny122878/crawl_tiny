import logging

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logFileName = 'errorLog.log'
logging.basicConfig(level=logging.ERROR, filename=logFileName, filemode='w', format=FORMAT)

def ErrorHandle(msg):
    logging.exception(msg)
    return True

def CheckErrorHint(hasError):
    if hasError:
        print("Process occur exception please check:",logFileName)
    else:
        print("Process done.")