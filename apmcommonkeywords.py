# APM Common Keywords.
from RFAtomLibrary import CommonUIKeywords
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from RFAtomLibrary.Apply.commonlocators import CommonLocators
from RFAtomLibrary.APM.commonlocatorsapm import CommonLocatorsAPM
from time import sleep

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
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.USERNAME_ID) +
                            "').value ='" + str(username) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        self.driver.execute_script("document.getElementById('" + self.get_locator_value(CommonLocatorsAPM.PASSWORD_ID) +
                                   "').value ='" + str(password) + "'")
        sleep(3)
        self.javascript_click(locator=CommonLocatorsAPM.CONTINUE_BUTTON)
        sleep(3)
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.USER_NAME, timeout=30)
        if not self.get_webelement(CommonLocatorsAPM.USER_NAME).is_displayed():
            self.fail(msg=f'Log in to APM is not completed by provided ${username} and ${password}')
        else:
            print("Login Successful\ntest case 1 is passed")
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
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.DASHBOARD_SELECT_BOX, timeout=30)
        if not self.get_webelement(CommonLocatorsAPM.DASHBOARD_SELECT_BOX).is_displayed():
            self.fail(msg=f'verify dashboard select box is not found')
        else:
            print("dashbox select box found\ntest case 2 is passed")
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
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.DASHBOARD_SELECT_BOX, timeout=30)
        if not self.get_webelement(CommonLocatorsAPM.DASHBOARD_SELECT_BOX).is_displayed():
            self.fail(msg=f'dashboard select box is not found')
        else:
            print("dashbox select box found\ntest case 3 is passed")

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
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.LIVE_SWITCH, timeout=30)
        if not self.get_webelement(CommonLocatorsAPM.LIVE_SWITCH).is_displayed():
            self.fail(msg=f'live switch is not found')
        elif self.get_webelement(CommonLocatorsAPM.LIVE_SWITCH_ON).is_displayed():
            self.javascript_click(locator=CommonLocatorsAPM.LIVE_SWITCH_ON)
            if self.get_webelement(CommonLocatorsAPM.LIVE_SWITCH_OFF).is_displayed():
                 print("Live switch is found and working \ntest case 4 is passed")
            else:
                print("Live Switch is not working")
        else:
            print("Live switch is not found")
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
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.CALENDAR_WIDGET, timeout=30)
        if not self.get_webelement(CommonLocatorsAPM.CALENDAR_WIDGET).is_displayed():
            self.fail(msg=f'calender widget is not found')
        else:
            print("calendar widget is found\ntest case 5 is passed")

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
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_APPLY_BUTTON, timeout=30)
        if not self.get_webelement(CommonLocatorsAPM.GO_TO_APPLY_BUTTON).is_displayed():
            self.fail(msg=f'Go to Appy button in Apply is not found')
        else:
            print("Go to Apply button in Apply is found\ntest case 6 is passed")

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
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_HSI_BUTTON, timeout=30)
        if not self.get_webelement(CommonLocatorsAPM.GO_TO_HSI_BUTTON).is_displayed():
            self.fail(msg=f'Go Diagnostics tool button in HSI is not found')
        else:
            print("Go Diagnostics tool button in HSI is found\ntest case 7 is passed")

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
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_JOB_SYNC_BUTTON, timeout=30)
        if not self.get_webelement(CommonLocatorsAPM.GO_TO_JOB_SYNC_BUTTON).is_displayed():
            self.fail(msg=f'Go to job sync button in job sync is not found')
        else:
          print("Go to job sync button in job sync is found\ntest case 8 is passed")
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
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_GRAFANA_BUTTON, timeout=30)
        if not self.get_webelement(
            CommonLocatorsAPM.GO_TO_GRAFANA_BUTTON).is_displayed():
            self.fail(msg=f'calender widget is not found')
        else:
            print("calendar widget is found\ntest case 9 is passed")
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
        self.wait_until_element_is_visible(locator=CommonLocatorsAPM.GO_TO_CHATBOT_BUTTON, timeout=100)
        if not self.get_webelement(
                CommonLocatorsAPM.GO_TO_CHATBOT_BUTTON).is_displayed():
            self.fail(msg=f'calender widget is not found')
        else:
            print("calendar widget is found\ntest case 10 is passed")

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
'''
obj.launch_browser(url="https://apm-stg.phenom.com")
obj.login_to_apm(username="rajasekhar.sandra@phenompeople.com", password="Sandra@455972")
obj.launch_browser(url="https://apm.phenom.com")
obj.verify_dashboard_select_box(username="rajasekhar.sandra@phenompeople.com", password="Sandra@455972")
obj.launch_browser(url="https://apm.phenom.com")
obj.validate_monitoring_dashboard_select_box(username="rajasekhar.sandra@phenompeople.com", password="Sandra@455972")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_live_switch(username="rajasekhar.sandra@phenompeople.com", password="Sandra@455972")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_calendar_widget(username="rajasekhar.sandra@phenompeople.com", password="Sandra@455972")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_go_to_apply_button_in_apply(username="rajasekhar.sandra@phenompeople.com", password="Sandra@455972")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_go_diagnostics_tool_button_in_hsi(username="rajasekhar.sandra@phenompeople.com", password="Sandra@455972")
'''
obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_go_to_job_sync_button_in_job_sync(username="rajasekhar.sandra@phenompeople.com", password="Sandra@455972")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_go_to_grafana_button_in_infrastructure(username="rajasekhar.sandra@phenompeople.com", password="Sandra@455972")

obj.launch_browser(url="https://apm-stg.phenom.com")
obj.verify_go_to_chatbot_button_in_chatbot(username="rajasekhar.sandra@phenompeople.com", password="Sandra@455972")
