import os
import threading
import shutil

SAVEDIR = '/Users/joachim/Library/Application Support/Pillars of Eternity/Saved Games/'
COPYDIR = SAVEDIR + 'saved/'

def isSaveGame(fileName):
    elements = os.path.splitext(fileName)
    if elements[1] == '.savegame':
        return True
    else:
        return False

def hasBeenSaved(fileName, savedFiles):
    if fileName not in savedFiles:
        shutil.copyfile(os.path.join(SAVEDIR, fileName), os.path.join(COPYDIR, fileName))
        print 'Saved: ' + fileName
    return

def saveMePls():
    threading.Timer(10.0, saveMePls).start()
    files = os.listdir(SAVEDIR)
    filesSaved = os.listdir(COPYDIR)
    
    for f in files:
        if isSaveGame(f):
            hasBeenSaved(f, filesSaved)
    return

saveMePls()