import RPi.GPIO as GPIO

class GPIOLib(object):

    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        pass

    def setModeGPIO(self, Mode): 
        GPIO.setmode(Mode)
        #This function is used to set the mode on which the GPIO
        #functions will be based on.
        #The two different modes are: GPIO.BOARD and GPIO:BCM
        #GPIO.BOARD means that you have to refer to the pins by
        #the pin number relative to the board.
        #GPIO.BCM means that you have to refer to the pins by
        #the GPIO number.
        #Refer to this link for a better understanding
        #https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_4b_4p0_reduced.pdf
        #The pin which is declared as GPIO_GEN0 will be refered to as
        #'11' if your mode is GPIO.BOARD, and refered to as '17' if
        #your mode is GPIO.BCM
        
    def InOrOutPin(self, Nr, Mode):
        GPIO.setup(Nr, Mode)
        #This function is used to declare the specified pin as an input
        #or an output pin. The number is which pin, and that depends on
        #the mode that was declared in the "SetModeGPIO" function.
        
    def SetOutValue(self, Nr, Value):
        if Value == 1 | Value == 0:
            GPIO.output(Nr, Value)
        else:
            print("Invalid!")
        #This function is used to tell the declared output pin which state
        #it should enter, '1' for High and '0' for Low
        #The number is which pin, and depends on the mode. (GPIO.BOARD/GPIO.BCM)
            
    def ReadInValue(self, Nr):
        return GPIO.input(Nr)
        #This function is used to read the input value on a specified pin.
        #The number is which pin, and depends on the mode. (GPIO.BOARD/GPIO.BCM)
            
    def CleanGPIO(self):
        GPIO.cleanup()
        #This function is used to reset the GPIO pins that has been set,
        #all the declared GPIO pins will be set to inputs.
        #This is a safety measure, so you don't accidentally fry the circuits.
        