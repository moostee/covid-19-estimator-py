import os.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def writeToFile(requestMethod, requestPath, statusCode, timeTaken):
    
    if not os.path.isfile(os.path.join(BASE_DIR, 'loggs.txt')):
        file = open(os.path.join(BASE_DIR, 'loggs.txt'), "x")

    file = open(os.path.join(BASE_DIR, 'loggs.txt'), "a")
    file.write(r'{}  {}  {}   {} ms{}'.format(requestMethod, requestPath, statusCode, timeTaken, '\n'))
    file.close()
    return

def readFile():
    file = open(os.path.join(BASE_DIR, 'loggs.txt'), "r")  
    return file.read() 