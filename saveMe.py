import os
import threading
import shutil

def isSaveGame(fileName):
    elements = os.path.splitext(fileName)
    if elements[1] == '.savegame':
        return True
    else:
        return False

def hasBeenSaved(fileName, savedFiles):
    if fileName not in savedFiles:
        shutil.copyfile(os.path.join('C:\Users\Joachim\Saved Games\Pillars of Eternity', fileName), os.path.join('C:\Users\Joachim\Saved Games\Pillars of Eternity\saved', fileName))
        print 'Saved: ' + fileName
    return

def saveMePls():
    threading.Timer(10.0, saveMePls).start()
    files = os.listdir('.')
    filesSaved = os.listdir('saved')
    
    for f in files:
        if isSaveGame(f):
            hasBeenSaved(f, filesSaved)
    return

saveMePls()
