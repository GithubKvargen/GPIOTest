*** Settings ***
Documentation    Version of the Robotframework Test
Library    testLib



*** Variables ***  
${18}=    ${18}
${24}=    ${24}
${On}=    ${1}
${Off}=    ${0}



*** Test Cases ***
First
    
    ${result3}=    Convert To Integer    ${24}
    ${Pin24}=    Set In Pin    ${result3}
    ${result}=    Convert To Integer    ${18}  
    ${Pin18}=    Set Out Pin    ${result}
    Turn On Pin    ${Pin18}
    ${result2}=    Convert To Integer    ${On}    
    Sleep    1    
    ${PinVal}=    Read In Pin    ${Pin24}
    Sleep    1    
    Run Keyword If    ${PinVal}==${On}    Echo    
    Sleep    1    
    

*** Keywords ***
Echo
    Log    "This is true"    
    
Echo2
    Log    "This is false"
    
