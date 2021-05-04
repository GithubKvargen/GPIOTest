*** Settings ***
Documentation    Version of the Robotframework Test
Library    testLib



*** Variables ***  
${Pin18}=    ${18}
${Pin24}=    ${24}
${On}=    ${1}
${Off}=    ${0}



*** Test Cases ***
First
    ${result}=    Convert To Integer    ${Pin18} 
    ${result2}=    Convert To Integer    ${On}    
    ${result3}=    Convert To Integer    ${Pin24}    
    Conf Out Pin    ${result}    ${result2}
    Conf In Pin    ${result3}
    Sleep    1    
    ${PinVal}=    Read In Pin    ${result3}
    Sleep    1    
    Run Keyword If    ${PinVal}==1    Echo    
    Sleep    1    
    

*** Keywords ***
Echo
    Log    "This is true"    
    
Echo2
    Log    "This is false"
    
