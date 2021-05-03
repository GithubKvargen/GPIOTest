*** Settings ***
Documentation    Version of the Robotframework Test
Library    testLib


*** Variables ***  


*** Test Cases ***
First
    Conf Out Pin    17    1
    ${PinVal}=    Read In Pin    17
    Run Keyword If    ${PinVal}==True    Echo    
    Run Keyword If    ${PinVal}==False    Echo2 

*** Keywords ***
Echo
    Log    "This is true"    
    
Echo2
    Log    "This is false"
    

