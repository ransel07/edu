import os
import platform
import time

def llamada(telefon_number, tm):
    
    comando = f"adb shell am start -a android.intent.action.CALL -d tel:{telefon_number}"
    
    os.system(comando)
    time.sleep(tm)
    
    os.system("adb shell input keyevent 6")


    time_hour = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
    nombre_archivo = f"llamada_{telefon_number}_{time_hour}.wav"
    os.system(f"adb pull /path/on/device {nombre_archivo}")
