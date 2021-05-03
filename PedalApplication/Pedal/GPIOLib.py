import gpiozero as GPIO
from gpiozero.output_devices import LED
from gpiozero.input_devices import Button

class GPIOLib(object):

    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self, MODE, Nr):
        if(MODE == "OUT"):
            self.__Mode = LED(Nr)
            self.__Value = Value
        else:
            self.__Mode = Button(Nr)
            self.__Value = Value

  #  def setModeGPIO(self, Mode): 
   #     GPIO.setmode(Mode)
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
        
    def TurnOnOutPin(self):
            self.__Mode.on()
        #This function is used to declare the specified pin as an input
        #or an output pin. The number is which pin, and that depends on
        #the mode that was declared in the "SetModeGPIO" function.
        
    def TurnOffOutPin(self):
        self.__Mode.off()

    def ReadInPin(self):
        return self.__Mode.is_active()
            
        