# cape_manager.py 
# Part of PyBBIO
# github.com/alexanderhiam/PyBBIO
# Apache 2.0 license
# 
# Beaglebone Cape Manager driver
# For Beaglebone's with 3.8 kernel or greater

from config import SLOTS_FILE
from bbio.util import addToCleanup

def load(overlay):
  """ Attempt to load an overlay with the given name. """ 
  with open(SLOTS_FILE, 'wb') as f:
    f.write(overlay)
  addToCleanup(lambda: unload(overlay))
    
def unload(overlay):
  """ Unload the first overlay matching the given name if present. Returns 
      True if successful, False if no mathcing overlay loaded. """ 
  with open(SLOTS_FILE, 'rb') as f:
    slots = f.readlines()
  for slot in slots:
    if overlay in slot:
      load('-%s' % slot.split(':')[0])
      return True
  return False 