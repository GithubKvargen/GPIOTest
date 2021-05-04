import gpiozero
from gpiozero.output_devices import LED
from gpiozero.input_devices import Button

class testLib(object):

    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        
        pass


    def SetOutPin(self, Nr):
        led = LED(Nr)
        print(led.value)
        print(led.pin)
        return led
    
    def SetInPin(self, Nr):
        btn = Button(Nr)
        print(btn.value)
        print(btn.pin)
        return btn
    
    def TurnOnPin(self, LED):
        print(LED.value)
        LED.on()
        print(LED.value)
        print(LED.pin)
        
    def TurnOffPin(self, LED):
        print(LED.value)
        LED.off()
        print(LED.value)
        print(LED.pin)
        
    def ReadInPin(self, Button):
        print(Button.pin)
        print(Button.value)
        return int(Button.value)
    
    def ShutdownOutPin(self, LED):
        print(LED.value)
        print(LED.pin)
        LED.close()
        print(LED.value)
        print(LED.pin)
        
    def ShutdownInPin(self, Button):
        print(Button.value)
        print(Button.pin)
        Button.close()
        print(Button.value)
        print(Button.pin)

                