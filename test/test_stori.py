from pathlib import PurePosixPath, Path

import allure
import pytest
from selenium.common import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test.base_test_helper import BaseTestHelper

STEPS_RTM_DIR = PurePosixPath.joinpath(Path(__file__).parent.parent).joinpath('steps_rtm')


@allure.suite("Stori Test Suite")
class StoriTestSuite(BaseTestHelper):
    @allure.title("Test Home Page")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.run(order=1)
    def test_home_page_1(self):
        self.open_browser_url("https://rahulshettyacademy.com/AutomationPractice/")
        self.assertion_text_element("Practice Page", "//body//h1")
        self.tearDown_()
        dict_test_home_page = {
            "test_case_id": "STORI-0001",
            "developer": "Maxi Correa",
            "test_group": "Stori QA",
            "test_case_name": "Validate home page",
            "priority_severity": "CRITICAL",
            "pre_conditions": "Have a Google chrome installed",
            "test_data": "https://rahulshettyacademy.com/AutomationPractice/",
            "test_steps": self.get_steps_from_step_rtm(),
            "expected_result": "The page MUST be load correctly and MUST be displayed Practice Page title",
            "tester": "Maxi Correa",
            "actual_result": self.get_actual_result(),
            "status": self.get_status_test(),
            "comments": "N/A",
            "test_evidence": "img"
        }
        self.set_rtm_with_data(dict_test_home_page)

    @allure.title("Test Suggestion Class Example")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=2)
    def test_suggestion_class_example_2(self):
        self.open_browser_url("https://rahulshettyacademy.com/AutomationPractice/")
        self.assert_element_("//input[@id='autocomplete']")
        self.type_("//input[@id='autocomplete']", "Me")
        self.sleep_(2)
        self.click_on_element("//ul[@id='ui-id-1']//*[text()='Mexico']")
        self.sleep_(5)
        self.tearDown_()
        dict_test_home_page = {
            "test_case_id": "STORI-0002",
            "developer": "Maxi Correa",
            "test_group": "Stori QA",
            "test_case_name": "Validate suggestion class example",
            "priority_severity": "NORMAL",
            "pre_conditions": "Have a Google chrome installed",
            "test_data": "https://rahulshettyacademy.com/AutomationPractice/",
            "test_steps": self.get_steps_from_step_rtm(),
            "expected_result": "The search input Suggestion Class Example MUST show the word Mexico",
            "tester": "Maxi Correa",
            "actual_result": self.get_actual_result(),
            "status": self.get_status_test(),
            "comments": "N/A",
            "test_evidence": "img"
        }
        self.set_rtm_with_data(dict_test_home_page)

    @allure.title("Test Dropdown Example")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=3)
    def test_dropdown_example_3(self):
        self.open_browser_url("https://rahulshettyacademy.com/AutomationPractice/")
        self.click_on_element("//select[@id='dropdown-class-example']")
        self.click_on_element("//option[contains(text(),'Option2')]")
        self.click_on_element("//body")
        self.sleep_(3)
        self.click_on_element("//select[@id='dropdown-class-example']")
        self.click_on_element("//option[contains(text(),'Option3')]")
        self.click_on_element("//body")
        self.sleep_(5)
        self.tearDown_()
        dict_test_home_page = {
            "test_case_id": "STORI-0003",
            "developer": "Maxi Correa",
            "test_group": "Stori QA",
            "test_case_name": "Validate Dropdown Example",
            "priority_severity": "MINOR",
            "pre_conditions": "Have a Google chrome installed",
            "test_data": "https://rahulshettyacademy.com/AutomationPractice/",
            "test_steps": self.get_steps_from_step_rtm(),
            "expected_result": "Option two MUST be displayed, then option three be displayed",
            "tester": "Maxi Correa",
            "actual_result": self.get_actual_result(),
            "status": self.get_status_test(),
            "comments": "N/A",
            "test_evidence": "img"
        }
        self.set_rtm_with_data(dict_test_home_page)

    """This test is commented so that the tests execution is valid"""

    # @allure.title("Test Switch Windows Example")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.run(order=4)
    # def test_switch_windows_example(self):
    #     self.open_browser_url("https://rahulshettyacademy.com/AutomationPractice/")
    #     self.click_on_element("//button[@id='openwindow']")
    #     search_text = "30 day money back guarantee"
    #     self.search_text_in_page(1, search_text)
    #     self.tearDown_()
    #     dict_test_home_page = {
    #         "test_case_id": "STORI-0004",
    #         "developer": "Maxi Correa",
    #         "test_group": "Stori QA",
    #         "test_case_name": "Validate switch windows example",
    #         "priority_severity": "MINOR",
    #         "pre_conditions": "Have a Google chrome installed",
    #         "test_data": "https://rahulshettyacademy.com/AutomationPractice/\n30 day money back guarantee",
    #         "test_steps": self.get_steps_from_step_rtm(),
    #         "expected_result": "Not encounter text and fail test",
    #         "tester": "Maxi Correa",
    #         "actual_result": self.get_actual_result(),
    #         "status": self.get_status_test(),
    #         "comments": "N/A",
    #         "test_evidence": "img"
    #     }
    #     self.set_rtm_with_data(dict_test_home_page)


    @allure.title("Test Switch To Tab Example")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=5)
    def test_switch_to_tab_example(self):
        self.open_browser_url("https://rahulshettyacademy.com/AutomationPractice/")
        self.click_on_element("//select[@id='dropdown-class-example']")
        self.click_on_element("//a[@id='opentab']")
        self.switch_to_tab_in_browser(1)
        self.sleep_(3)
        self.save_screenshot_to_dir("Test_Switch_to_Tab_Example", STEPS_RTM_DIR, "//a[contains(text(),'Access all our Courses')]")
        self.sleep_(1)
        self.switch_to_window(0)
        self.tearDown_()
        dict_test_home_page = {
            "test_case_id": "STORI-0005",
            "developer": "Maxi Correa",
            "test_group": "Stori QA",
            "test_case_name": "Test Switch to Tab Example",
            "priority_severity": "MINOR",
            "pre_conditions": "Have a Google chrome installed",
            "test_data": "https://rahulshettyacademy.com/AutomationPractice/",
            "test_steps": self.get_steps_from_step_rtm(),
            "expected_result": "Save the button screenshot in expecific path",
            "tester": "Maxi Correa",
            "actual_result": self.get_actual_result(),
            "status": self.get_status_test(),
            "comments": "N/A",
            "test_evidence": "img"
        }
        self.set_rtm_with_data(dict_test_home_page)

    @allure.title("Test Switch To Alert Example")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=6)
    def test_switch_to_alert_example(self):
        self.open_browser_url("https://rahulshettyacademy.com/AutomationPractice/")
        self.type_("//input[@id='name']", "Stori Card")
        self.click("//input[@id='alertbtn']")
        try:
            wait = WebDriverWait(self.get_new_driver("chrome"), 10)
            alert = wait.until(expected_conditions.alert_is_present())
            alert_text = alert.text
            text = "Hello Stori Card, share this practice page and share your knowledge"
            assert alert_text == text
            alert.accept()
            self.sleep_(5)

            self.type_("//input[@id='name']", text)
            self.click_on_element("//input[@id='confirmbtn']")
            alert2 = wait.until(expected_conditions.alert_is_present())
            alert_text2 = alert2.text
            text2 = "Hello Hello Stori Card, share this practice page and share your knowledge, Are you sure you want to confirm?"
            assert text2 == alert_text2
        except (NoAlertPresentException, TimeoutException):
            print("No alert found or an error occurred while interacting with the alert.")
        self.tearDown_()
        dict_test_home_page = {
            "test_case_id": "STORI-0006",
            "developer": "Maxi Correa",
            "test_group": "Stori QA",
            "test_case_name": "Test Switch to Alert Example",
            "priority_severity": "MINOR",
            "pre_conditions": "Have a Google chrome installed",
            "test_data": "https://rahulshettyacademy.com/AutomationPractice/\nTEXT_TO_VALIDATE: Hello Hello Stori Card, share this practice page and share your knowledge, Are you sure you want to confirm?",
            "test_steps": self.get_steps_from_step_rtm(),
            "expected_result": "The second text MUST be see in the alert message",
            "tester": "Maxi Correa",
            "actual_result": self.get_actual_result(),
            "status": self.get_status_test(),
            "comments": "N/A",
            "test_evidence": "img"
        }
        self.set_rtm_with_data(dict_test_home_page)

    @allure.title("Test Web Table Example")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=7)
    def test_web_table_example(self):
        self.open_browser_url("https://rahulshettyacademy.com/AutomationPractice/")

        list_courses = self.find_elements_to_list("//table[@name='courses']//tr/td[2]")
        list_prices = self.find_elements_to_list("//table[@name='courses']//tr/td[2]/following-sibling::td")

        self.iter_lists_for_course(list_courses, list_prices, value=25)
        self.tearDown_()
        dict_test_home_page = {
            "test_case_id": "STORI-0007",
            "developer": "Maxi Correa",
            "test_group": "Stori QA",
            "test_case_name": "Test Web Table Example",
            "priority_severity": "MINOR",
            "pre_conditions": "Have a Google chrome installed",
            "test_data": "https://rahulshettyacademy.com/AutomationPractice/",
            "test_steps": self.get_steps_from_step_rtm(),
            "expected_result": "Print the number of courses that are $25, and their names",
            "tester": "Maxi Correa",
            "actual_result": self.get_actual_result(),
            "status": self.get_status_test(),
            "comments": "N/A",
            "test_evidence": "img"
        }
        self.set_rtm_with_data(dict_test_home_page)

    @allure.title("Test Web Table Fixed Header Example")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=8)
    def test_web_table_fixed_header(self):
        self.open_browser_url("https://rahulshettyacademy.com/AutomationPractice/")

        list_elements = self.find_elements_to_list("//div[@class='tableFixHead']//table//tbody/tr")
        self.scroll_to_element("//legend[contains(text(),'Web Table Fixed header')]")

        persons = []

        for element in list_elements:
            elements_split = element.text.split(" ")
            if len(elements_split) == 4:
                name, position, city, amount = elements_split
                person = Person(name, position, city, amount)
                persons.append(person)
            else:
                continue

        for person in persons:
            if person.position == "Engineer":
                print(f"Engineer name: {person.name}")

        self.tearDown_()
        dict_test_home_page = {
            "test_case_id": "STORI-0008",
            "developer": "Maxi Correa",
            "test_group": "Stori QA",
            "test_case_name": "Test Web Table Fixed Header Example",
            "priority_severity": "NORMAL",
            "pre_conditions": "Have a Google chrome installed",
            "test_data": "https://rahulshettyacademy.com/AutomationPractice/",
            "test_steps": self.get_steps_from_step_rtm(),
            "expected_result": "Print name of the engineers",
            "tester": "Maxi Correa",
            "actual_result": self.get_actual_result(),
            "status": self.get_status_test(),
            "comments": "N/A",
            "test_evidence": "img"
        }
        self.set_rtm_with_data(dict_test_home_page)

    @allure.title("Test iFrame Example")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=9)
    def test_iframe_example(self):
        self.open_browser_url("https://rahulshettyacademy.com/AutomationPractice/")
        self.switch_to_frame_("//iframe[@id='courses-iframe']")
        self.scroll_to_element("//*/div[@class='price-title']/h2/span[contains(text(),'why we are')]")
        list_text = self.find_elements_to_list("//*/div[@class='row clearfix']/div/ul[@class='list-style-two']/li")

        texts = []

        for element in list_text:
            elements_split = element.text.split(". ")
            if len(elements_split) == 1:
                texts.append(elements_split)

        print(f"TEXT: {texts[10]}")
        print("********************************************************")
        for index, text in enumerate(texts):
            if index % 2 != 0:
                print(f"I AM IMPAR: {text}")
                print()

        self.tearDown_()
        dict_test_home_page = {
            "test_case_id": "STORI-0009",
            "developer": "Maxi Correa",
            "test_group": "Stori QA",
            "test_case_name": "Test iFrame Example",
            "priority_severity": "NORMAL",
            "pre_conditions": "Have a Google chrome installed",
            "test_data": "https://rahulshettyacademy.com/AutomationPractice/",
            "test_steps": self.get_steps_from_step_rtm(),
            "expected_result": "Print name of the engineers",
            "tester": "Maxi Correa",
            "actual_result": self.get_actual_result(),
            "status": self.get_status_test(),
            "comments": "N/A",
            "test_evidence": "img"
        }
        self.set_rtm_with_data(dict_test_home_page)


class Person:
    def __init__(self, name, position, city, amount):
        self.name = name
        self.position = position
        self.city = city
        self.amount = amount

    def __str__(self):
        return f"Person(name={self.name}, position={self.position}, city={self.city}, amount={self.amount})"

