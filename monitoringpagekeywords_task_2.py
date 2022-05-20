# APM Common Keywords.
from RFAtomLibrary import CommonUIKeywords
from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn
from RFAtomLibrary.Apply.commonlocators import CommonLocators
from RFAtomLibrary.APM.commonlocatorsapm import CommonLocatorsAPM
from time import sleep
from RFAtomLibrary.APM.apmurls_task_2 import ApmUrls

from RFAtomLibrary.APM.credentials_task_2 import Credentials

@library
class ApmCommonKeywords(CommonUIKeywords, BuiltIn):
    """ APM Common keywords"""

    @keyword("Login to APM")
    def login_to_apm(self,
                     username: str,
                     password: str):
        """
            Login to APM by username and password.
            :return: :raise Exception if login does not happened.
        Examples:
        | Login to APM | username    |   password
        """
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                                   "').value ='" + str(username) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.wait_until_element_is_visible(
            locator=self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID), timeout=30,
            error=f'Locator : {self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID)} is not visible after action')
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                                   "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)

        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.USER_NAME, timeout=30,
                                           error=f'Log in to APM is not completed by provided ${username} and ${password}')
        self.log("Login Successful\ntest case 1 is passed")


    @keyword("verify dashboard select box")
    def verify_dashboard_select_box(self):
        """
           verify dashboard select box found or not

            :return: :raise Exception if dashboard select box not found.
        """
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.DASHBOARD_SELECT_BOX, timeout=30,
                                           error=f'verify dashboard select box is not found')
        self.log("dashbox select box found\ntest case 2 is passed")


    @keyword("validate monitoring dashboard select box")
    def validate_monitoring_dashboard_select_box(self):
        """
        verify dashboard select box working or not.

        :return: :raise Exception if dashboard select box does not working.
        """
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.DASHBOARD_SELECT_BOX, timeout=30,
                                           error=f'dashboard select box is not found')
        self.log("dashbox select box found\ntest case 3 is passed")

    @keyword("verify live switch")
    def verify_live_switch(self):
        """
        verify live switch button is working or not.

        :return: raise Exception if live switch does not working.
        """
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.LIVE_SWITCH, timeout=30,
                                           error=f'live switch is not found')
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.LIVE_SWITCH_ON, timeout=30,
                                           error=f'live switch should be on by default')
        self.javascript_click(locator=CommonLocatorsAPM.LIVE_SWITCH_ON)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.LIVE_SWITCH_OFF, timeout=30,
                                           error=f'Live Switch is not working')
        self.log("Live switch is found and working \ntest case 4 is passed")

    @keyword("verify calendar widget")
    def verify_calendar_widget(self):
        """
        verify calendar widget is working or not.

        :return: :raise Exception if calendar widget is not found
        """
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.CALENDAR_WIDGET, timeout=30,
                                           error=f'calender widget is not found')
        self.log("calendar widget is found\ntest case 5 is passed")

    @keyword("Verify Go to Appy button in Apply")
    def verify_go_to_apply_button_in_apply(self):
        """
        verify go to apply button is working or not.

        :return: :raise Exception if go to apply does not working
        """

        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_APPLY_BUTTON, timeout=30,
                                           error=f'Go to Appy button in Apply is not found')
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.GO_TO_APPLY_BUTTON)
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        #print(self.driver.current_url, ApmUrls.apply_url)
        if self.driver.current_url == ApmUrls.apply_url:
            self.log("Go to Apply button in Apply is working\ntest case 6 is passed")
        else:
            self.fail(msg=f'go to apply button is not working')


    @keyword("Verify Go Diagnostics tool button in HSI")
    def verify_go_diagnostics_tool_button_in_hsi(self):
        """
                verify go to HSI button is working or not.

                :return: :raise Exception if go to HSI BUTTON does not working
        """

        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_HSI_BUTTON, timeout=30,
                                           error=f'Go Diagnostics tool button in HSI is not found')
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.GO_TO_HSI_BUTTON)
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        #print(self.driver.current_url,ApmUrls.hsi_url)


        if self.driver.current_url == ApmUrls.hsi_url:
            self.log("Go to HSI button in HSI is working\ntest case 7 is passed")
        else:
            self.fail(msg=f'Go to HSI button in HSI is not working')

    @keyword("Verify Go to Job Sync button in Job sync")
    def verify_go_to_job_sync_button_in_job_sync(self):
        """
                verify go to JOB SYNC button is working or not.

                :return: :raise Exception if go to JOB SYNC does not working
        """

        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_JOB_SYNC_BUTTON, timeout=30,
                                           error=f'Go to job sync button in job sync is not found')
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.GO_TO_JOB_SYNC_BUTTON)
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        #print(self.driver.current_url,ApmUrls.job_sync_url)
        if self.driver.current_url == ApmUrls.job_sync_url:
            self.log("Go to job sync button in job sync is working\ntest case 8 is passed")
        else:
            self.fail(msg=f'Go to job sync button in job sync is not working')


    @keyword("Verify Go to Grafana button in Infrastructure")
    def verify_go_to_grafana_button_in_infrastructure(self):
        """
                verify go to GRAFANA button is working or not.

                :return: :raise Exception if go to GRAFANA button does not working
        """

        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_GRAFANA_BUTTON, timeout=30,
                                           error=f'go to grafana button in infrastructure is not found')
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.GO_TO_GRAFANA_BUTTON)
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        #print(self.driver.current_url,ApmUrls.grafana_url)
        if self.driver.current_url == ApmUrls.grafana_url:
            self.log("go to grafana button in infrastructure is working\ntest case 9 is passed")
        else:
            self.fail(msg=f"go to grafana button in infrastructure is not working")


    @keyword("Verify Go to Chatbot button in Chatbot")
    def verify_go_to_chatbot_button_in_chatbot(self):
        """
                verify go to CHATBOT button is working or not.

                :return: :raise Exception if go to CHATBOT button does not work
        """

        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_CHATBOT_BUTTON, timeout=100,
                                           error=f'go to chatbot button is not found')
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.GO_TO_CHATBOT_BUTTON)
        sleep(3)
        #print(self.driver.current_url)

        self.driver.switch_to.window(self.driver.window_handles[1])
        if self.get_webelement("xpath=//input[@id='domain']").is_displayed():
            self.log("go to chatbot button in chatbot is working\ntest case 10 is passed")
        else:
            self.fail(msg=f"go to chatbot button in chatbot is not working")

    @keyword("verify create dashboard toolkit")
    def verify_create_dashboard_toolkit(self):
        """
        verify create dashboard toolkit

        :return: :raise Exception if create dashboard toolkit does not work
        """
        '''
        self.wait_until_element_is_visible(locator="xpath=//button[@class='ant-btn create-dashboard-btn']", timeout=30,
                                           error=f'error123')

        sleep(3)
        self.javascript_click(locator="xpath=//button[@class='ant-btn create-dashboard-btn']")
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.DASHBOARD_NAME, timeout=30, error=f'Dashboard name field not found in ui')
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.DASHBOARD_DROPDOWN, timeout=30,
                                           error=f'Dashboard dropdown is not found')
        temp = self.get_webelement(CommonLocatorsAPM.DASHBOARD_DROPDOWN).text
        print(self.get_webelement(CommonLocatorsAPM.DASHBOARD_DROPDOWN).text)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.DASHBOARD_NAME) +
                                   "').value ='" + str("sample dashboard") + "'")
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.CREATE_DASHBOARD_CANCEL_BUTTON, timeout=30, error=f'cancel button is not found in ui')
        self.javascript_click(locator=CommonLocatorsAPM.CREATE_DASHBOARD_CANCEL_BUTTON)

        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.DASHBOARD_DROPDOWN, timeout=30, error=f'Dashboard dropdown is not found')
        if not self.get_webelement(CommonLocatorsAPM.DASHBOARD_DROPDOWN).text == temp:
            print("In create dashboard popup cancel button is not working")
        else:
            print("In create dashboard popup cancel button is working")
            '''
        self.wait_until_element_is_visible(locator="xpath=//button[@class='ant-btn create-dashboard-btn']", timeout=30,
                                           error=f'error123')
        self.javascript_click(locator="xpath=//button[@class='ant-btn create-dashboard-btn']")
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.DASHBOARD_NAME, timeout=30,
                                           error=f'Dashboard name field not found in ui')
        sleep(3)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.DASHBOARD_NAME) +
            "').value ='" + str("sample dashboard") + "'")
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.CREATE_DASHBOARD_CREATE_BUTTON, timeout=30,
                                           error=f'create button is not found in ui')
        self.javascript_click(locator=CommonLocatorsAPM.CREATE_DASHBOARD_CREATE_BUTTON)
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.DASHBOARD_DROPDOWN, timeout=30,
                                           error=f'Dashboard dropdown is not found')
        sleep(3)
        print(self.get_webelement(CommonLocatorsAPM.DASHBOARD_DROPDOWN).text)
        if not self.get_webelement(CommonLocatorsAPM.DASHBOARD_DROPDOWN).text == "sample dashboard":
            print("In create dashboard popup create button is not working")
        else:
            print("create dashboard is working\ntest case 11 is passed")






    @keyword("verify kebab menu")
    def verify_kebab_menu(self):
        pass

    @keyword("verify add new section button")
    def verify_add_new_section_button(self):
        pass

    @keyword("verify add alerts")
    def verify_add_alerts(self):
        pass

    @keyword("Verify kebab menu in section level")
    def verify_kebab_menu_in_section_level(self):
        pass

    @keyword("verify kebab menu of particular product")
    def verify_kebab_menu_of_particular_product(self):
        pass


    def javascript_click(self, locator=None):
        """ Clicks any locator using java script .
                    Examples:
                    | JavaScript_Click | locator= <xpath=//xpath>
                """

        web_ele = self.get_webelement(locator=locator)
        self.driver.execute_script("arguments[0].click();", web_ele)

    def get_locator_value(self, locator=None):
        """ Get Locator Value
        Examples:
        | Get Locator Value | locator= <xpath=//xpath>
        | Get Locator Value | locator= <xpath=//xpath>
        """
        value = locator.split('=', 1)[1]
        return value

'''
obj = ApmCommonKeywords()

obj.launch_browser(url="https://apm-stg.phenom.com")

obj.login_to_apm(username=Credentials.username, password=Credentials.password)

obj.verify_dashboard_select_box()

obj.validate_monitoring_dashboard_select_box()

obj.verify_live_switch()

obj.verify_calendar_widget()

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.login_to_apm(username=Credentials.username, password=Credentials.password)
obj.verify_go_to_apply_button_in_apply()

#obj.driver.switch_to.window(obj.driver.window_handles[0])

#obj.launch_browser(url="https://apm-stg.phenom.com")
#obj.verify_go_diagnostics_tool_button_in_hsi()
#obj.driver.switch_to.window(obj.driver.window_handles[0])

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.login_to_apm(username=Credentials.username, password=Credentials.password)
obj.verify_go_to_job_sync_button_in_job_sync()

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.login_to_apm(username=Credentials.username, password=Credentials.password)
obj.verify_go_to_grafana_button_in_infrastructure()

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.login_to_apm(username=Credentials.username, password=Credentials.password)
obj.verify_go_to_chatbot_button_in_chatbot()
#obj.driver.switch_to.window(obj.driver.window_handles[0])

#obj.verify_create_dashboard_toolkit()
'''
