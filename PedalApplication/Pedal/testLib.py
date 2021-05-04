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
        
                
    #def ReadInPin(self, Nr):
    #    print("do we even get here?")
    #    if(Button(Nr).is_active()):
     #       print("Hello are we here?")
     #       return 1
     #   else:
      #      print("Maybe here?")
      #      return 0
        
    def SetOutPin(self, Nr):
        led = LED(Nr)
        return led
    
    def SetInPin(self, Nr):
        btn = Button(Nr)
        return btn
    
    def TurnOnPin(self, LED):
        LED.on()
        
    def TurnOffPin(self, LED):
        LED.off()
        
    def ReadInPin(self, Button):
        print("Do we get here?")
        if(Button.is_active()):
            print("We got it as active")
            return int(1)
        else:
            print("Nonono")
            return int(1)

                