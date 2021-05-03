*** Settings ***
Documentation    Version of the Robotframework Test
Library    testLib


*** Variables ***  


*** Test Cases ***
First
    Conf Out Pin    17    1
    Run Keyword If    Read In Pin[17]    Echo    

*** Keywords ***
Echo
    Log    "This is working"    
