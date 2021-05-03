*** Settings ***
Documentation    Version of the Robotframework Test
Library    testLib


*** Variables ***  


*** Test Cases ***
First
    Conf Out Pin    17    1
    Run Keyword If    getPin    Echo    

*** Keywords ***
Echo
    Log    "This is working"    
    
getPin
    ${PinVal}=    Read In Pin    17
    Convert To Boolean    ${PinVal}
    [Return]    ${PinVal}
