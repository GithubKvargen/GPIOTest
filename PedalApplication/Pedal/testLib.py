import gpiozero
from gpiozero.output_devices import LED
from gpiozero.input_devices import Button

class testLib(object):

    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        
        pass


    def SetOutPin(self, Nr):
        led = LED(Nr)
        return led
    
    def SetInPin(self, Nr):
        btn = Button(Nr)
        return btn
    
    def TurnOnPin(self, LED):
        print(LED.value)
        LED.on()
        print(LED.value)
        print(LED.pin)
        
    def TurnOffPin(self, LED):
        LED.off()
        
    def ReadInPin(self, Button):
        print(Button.pin)
        print(Button.is_active)
        return int(Button.value)
    
    def ShutdownOutPin(self, LED):
        LED.close()
        
    def ShutdownInPin(self, Button):
        Button.close()

                