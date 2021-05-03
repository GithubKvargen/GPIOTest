import gpiozero as GPIO
from gpiozero.output_devices import LED
from gpiozero.input_devices import Button

class GPIOLib(object):
    
    ROBOT_LIBRARY_VERSION = 1.0
    
    

    def __init__(self, MODE, Nr):
        if(MODE == "OUT"):
            self.__Mode = LED(Nr)
        else:
            self.__Mode = Button(Nr)
        pass
        
    def TurnOnOutPin(self):
            self.__Mode.on()

        
    def TurnOffOutPin(self):
        self.__Mode.off()

    def ReadInPin(self):
        return self.__Mode.is_active()
            
        