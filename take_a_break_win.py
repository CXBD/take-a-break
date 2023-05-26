import time
from ctypes import windll

while True:
  time.sleep(60*20) # 20 minutes
  LockScreen = windll.LoadLibrary('user32.dll')
  LockScreen.LockWorkStation()
