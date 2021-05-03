*** Settings ***
Documentation    Version of the Robotframework Test
Library    testLib


*** Variables ***  
${PinVal}

*** Test Cases ***
First
    Conf Out Pin    17    1
    ${PinVal}=    Read In Pin    17
    Run Keyword If    ${PinVal}    Echo    

*** Keywords ***
Echo
    Log    "This is true"    
    
Echo2
    Log    "This is false"
    
