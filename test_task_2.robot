*** Settings ***
Library     RFAtomLibrary.APM.apmcommonkeywords.ApmCommonKeywords
Test Setup  Launch_and_Login_to_APM

*** Variables ***
${url}    https://apm-stg.phenom.com
${browser}    Chrome
${username}   rajasekhar.sandra@phenompeople.com
${password}   Sandra@455972

*** Test Cases ***
al_ts01_tc01
    [Documentation]  Navigation to Monitoring Page with valid username and password
    [Tags]    functional
    verify dashboard select box
al_ts01_tc02
    [Documentation]  Navigation to Monitoring Page with valid username and password
    [Tags]    functional
    validate monitoring dashboard select box
al_ts01_tc03
    [Documentation]  Navigation to Monitoring Page with valid username and password
    [Tags]    functional
    verify live switch
al_ts01_tc04
    [Documentation]  Navigation to Monitoring Page with valid username and password
    [Tags]    functional
    verify calendar widget
al_ts01_tc05
    [Documentation]  Navigation to Monitoring Page with valid username and password
    [Tags]    functional
    verify go to appy button in apply
al_ts01_tc06
    [Documentation]  Navigation to Monitoring Page with valid username and password
    [Tags]    functional
    verify go to grafana button in infrastructure
al_ts01_tc07
    [Documentation]  Navigation to Monitoring Page with valid username and password
    [Tags]    functional
    verify go to job sync button in job sync
al_ts01_tc08
    [Documentation]  Navigation to Monitoring Page with valid username and password
    [Tags]    functional
    verify go diagnostics tool button in hsi
al_ts01_tc09
    [Documentation]  Navigation to Monitoring Page with valid username and password
    [Tags]    functional
    verify go to chatbot button in chatbot


*** Keywords ***
Launch_and_Login_to_APM
    Launch Browser    url=${url}
    Login to APM     username=${username}    password=${password}
