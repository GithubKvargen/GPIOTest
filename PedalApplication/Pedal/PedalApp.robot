*** Settings ***
Documentation    Version of the Robotframework Test
Library    testLib



*** Variables ***  
${Pin17}=    ${17}
${On}=    ${1}
${Off}=    ${0}



*** Test Cases ***
First
    ${result}=    Convert To Integer    ${Pin17} 
    ${result2}=    Convert To Integer    ${On}    
    Conf Out Pin    ${result}    ${result2}
    ${PinVal}=    Read In Pin    ${result}
    Run Keyword If    ${PinVal}==1    Echo    

*** Keywords ***
Echo
    Log    "This is true"    
    
Echo2
    Log    "This is false"
    
