import gpiozero
from gpiozero.output_devices import LED
from gpiozero.input_devices import Button

class testLib(object):

    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        
        pass

    def Hello(self):
        print("Hello There")
        
    def FUCK(self):
        print("FUCK")

    def ConfOutPin(self, Nr, Value):
            if(Value == 1):
                led = LED(Nr)
                led.on()
            else:
                led = LED(Nr)
                led.off()
                
    def ConfInPin(self, Nr):
        btn = Button(Nr)
        
                
    def ReadInPin(self, Nr):
        if(Button(Nr).is_active()):
            print("Hello are we here?")
            return 1
        else:
            print("Maybe here?")
            return 0

                