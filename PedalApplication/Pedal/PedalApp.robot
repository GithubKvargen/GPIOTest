*** Settings ***
Documentation    Version of the Robotframework Test
Library    testLib
Library    GPIOLib.py






*** Test Cases ***
First
    setModeGPIO("GPIO.BCM")
    InOrOutPin(17,"OUT")
    SetOutValue(17,1)
    Run Keyword If    ReadInValue(17)    Echo    
    

    
*** Keywords ***
Echo
    Log    "This is working"    
