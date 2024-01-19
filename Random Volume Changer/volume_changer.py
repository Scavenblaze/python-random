from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import random

devices=AudioUtilities.GetSpeakers() #get speakers
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


#volume.SetMasterVolumeLevel(-2, None)  #-65 to 0

'''
(-65, None) makes vol 0
(0, None) 100% vol
-1 is 94%
-2 is 88
each 6 points it doubles
'''
while(True):
    ch=int(input("Enter 1 to change volume: "))
    if(ch==1):
        a=random.randint(-65, 0)
        volume.SetMasterVolumeLevel(a, None)
        vol=int(volume.GetMasterVolumeLevelScalar()*100)    #gets scalar value of current volume level and converts to %
        print("Current Volume: ", vol, "%")
    else:   print("I said 1")