# APM Common Keywords.
from RFAtomLibrary import CommonUIKeywords
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from RFAtomLibrary.Apply.commonlocators import CommonLocators
from RFAtomLibrary.APM.commonlocatorsapm import CommonLocatorsAPM
from time import sleep
from credentials import Credentials

class ApmCommonKeywords(CommonUIKeywords, BuiltIn):
    """ APM Common keywords"""

    @keyword("Login to APM")
    def login_to_apm(self,
                     username: str,
                     password: str):
        """Login to APM by username and password.

        :return: :raise Exception if login does not happened.
        Examples:
        | Login to APM | username    |   password
        """
        #self.wait_until_element_is_visible(
           # locator=self.get_locator_value(CommonLocatorsAPM.USERNAME_ID), timeout=30,
           # error=f'Locator : {self.get_locator_value(CommonLocatorsAPM.USERNAME_ID)} is not visible after action')
        sleep(3)
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
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.USER_NAME, timeout=30,error=f'Log in to APM is not completed by provided ${username} and ${password}')
        self.log("Login Successful\ntest case 1 is passed")
    @keyword("verify dashboard select box")
    def verify_dashboard_select_box(self,
                                    username: str,
                                    password: str):
        """Login to APM by username and password.
           verify dashboard select box found or not

        :return: :raise Exception if login does not happened or dashboard select box not found.
               """

        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                                   "').value ='" + str(username) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                                   "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.DASHBOARD_SELECT_BOX, timeout=30, error=f'verify dashboard select box is not found')
        self.log("dashbox select box found\ntest case 2 is passed")
    @keyword("validate monitoring dashboard select box")
    def validate_monitoring_dashboard_select_box(self,
                                                 username: str,
                                                 password: str):
        """
        Login to APM by username and password.
        verify dashboard select box working or not.

        :return: :raise Exception if login does not happened or dashaboard select box is not working
        """
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                                   "').value ='" + str(username) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                                   "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.DASHBOARD_SELECT_BOX, timeout=30, error=f'dashboard select box is not found')
        self.log("dashbox select box found\ntest case 3 is passed")

    @keyword("verify live switch")
    def verify_live_switch(self,
                           username: str,
                           password: str
                           ):
        """
        Login to APM by username and password.
        verify live switch button is working or not.

        :return: raise Exception if login does not happened or live switch is not working.
        """
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                                   "').value ='" + str(username) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                                   "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.LIVE_SWITCH, timeout=30, error=f'live switch is not found')
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.LIVE_SWITCH_ON, timeout=30,
                                           error=f'live switch should be on by default')
        self.javascript_click(locator=CommonLocatorsAPM.LIVE_SWITCH_ON)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.LIVE_SWITCH_OFF, timeout=30,
                                           error=f'Live Switch is not working')
        self.log("Live switch is found and working \ntest case 4 is passed")
    @keyword("verify calendar widget")
    def verify_calendar_widget(self,
                               username: str,
                               password: str):
        """
        Login to APM by username and password.
        verify calendar widget is working or not.

        :return: :raise Exception if login does not happened or calendar widget is not found
        """
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                                   "').value ='" + str(username) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                                   "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.CALENDAR_WIDGET, timeout=30,error=f'calender widget is not found')
        self.log("calendar widget is found\ntest case 5 is passed")

    @keyword("Verify Go to Appy button in Apply")
    def verify_go_to_apply_button_in_apply(self,
                                           username: str,
                                           password: str
                                           ):
        """
        Login to APM by username and password..
        verify go to apply button is working or not.

        :return: :raise Exception if login does not happened and go to apply is not working
        """

        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                                   "').value ='" + str(username) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                                   "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_APPLY_BUTTON, timeout=30, error=f'Go to Appy button in Apply is not found')
        self.log("Go to Apply button in Apply is found\ntest case 6 is passed")

    @keyword("Verify Go Diagnostics tool button in HSI")
    def verify_go_diagnostics_tool_button_in_hsi(self,
                                                 username: str,
                                                 password: str
                                                 ):
        """
                Login to APM by username and password..
                verify go to HSI button is working or not.

                :return: :raise Exception if login does not happened and go to HSI BUTTON is not working
        """
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                           "').value ='" + str(username) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                           "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_HSI_BUTTON, timeout=30,error=f'Go Diagnostics tool button in HSI is not found')
        self.log("Go Diagnostics tool button in HSI is found\ntest case 7 is passed")

    @keyword("Verify Go to Job Sync button in Job sync")
    def verify_go_to_job_sync_button_in_job_sync(self,
                                         username: str,
                                         password: str):
        """
                Login to APM by username and password..
                verify go to JOB SYNC button is working or not.

                :return: :raise Exception if login does not happened and go to JOB SYNC is not working
        """

        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                           "').value ='" + str(username) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                           "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_JOB_SYNC_BUTTON, timeout=30, error=f'Go to job sync button in job sync is not found')
        self.log("Go to job sync button in job sync is found\ntest case 8 is passed")

    @keyword("Verify Go to Grafana button in Infrastructure")
    def verify_go_to_grafana_button_in_infrastructure(self,
                                              username: str,
                                              password: str):
        """
                Login to APM by username and password..
                verify go to GRAFANA button is working or not.

                :return: :raise Exception if login does not happened and go to GRAFANA is not working
        """

        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                           "').value ='" + str(username) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                           "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_GRAFANA_BUTTON, timeout=30, error=f'calender widget is not found')
        self.log("calendar widget is found\ntest case 9 is passed")

    @keyword("Verify Go to Chatbot button in Chatbot")
    def verify_go_to_chatbot_button_in_chatbot(self,
                                       username: str,
                                       password: str):
        """
                Login to APM by username and password..
                verify go to CHATBOT button is working or not.

                :return: :raise Exception if login does not happened and go to CHATBOT is not working
        """
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                                   "').value ='" + str(username) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                                   "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_CHATBOT_BUTTON, timeout=100, error=f'calender widget is not found')
        self.log("calendar widget is found\ntest case 10 is passed")

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


obj = ApmCommonKeywords()

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.login_to_apm(username=Credentials.username, password=Credentials.password)

obj.launch_browser(url="https://apm.phenom.com")
obj.verify_dashboard_select_box(username=Credentials.username, password=Credentials.password)

obj.launch_browser(url="https://apm.phenom.com")
obj.validate_monitoring_dashboard_select_box(username=Credentials.username, password=Credentials.password)

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_live_switch(username=Credentials.username, password=Credentials.password)

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_calendar_widget(username=Credentials.username, password=Credentials.password)

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_go_to_apply_button_in_apply(username=Credentials.username, password=Credentials.password)

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_go_diagnostics_tool_button_in_hsi(username=Credentials.username, password=Credentials.password)

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_go_to_job_sync_button_in_job_sync(username=Credentials.username, password=Credentials.password)

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_go_to_grafana_button_in_infrastructure(username=Credentials.username, password=Credentials.password)

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_go_to_chatbot_button_in_chatbot(username=Credentials.username, password=Credentials.password)

