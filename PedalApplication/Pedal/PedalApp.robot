*** Settings ***
Documentation    Version of the Robotframework Test
Library    testLib


*** Variables ***


*** Test Cases ***

    
GPIOTest
    ${On}=    Convert To Integer    ${1}    
    ${Off}=    Convert To Integer    ${0}    
    ${int23}=    Convert To Integer    ${23}    
    ${int24}=    Convert To Integer    ${24}    
    ${Pin23}=    Set Out Pin    ${int23}
    ${Pin24}=    Set In Pin    ${int24}
    Turn Off Pin    ${Pin23}
    Sleep    1    
    Turn On Pin    ${Pin23}
    Sleep    1    
    ${result}=    Read In Pin    ${Pin24}
    Run Keyword If    ${result}==${On}    Echo    
    Sleep    2    
    Turn Off Pin    ${Pin23}
    Shutdown Out Pin    ${Pin23}
    Shutdown In Pin    ${Pin24}
    
    
    

*** Keywords ***
Echo
    Log    "This is true"    
    
Echo2
    Log    "This is false"
    
