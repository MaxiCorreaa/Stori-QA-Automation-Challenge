from seleniumbase import BaseCase

BaseCase.main(__name__, __file__)


class MyTestClass(BaseCase):
    def test_home_page_1(self):
        self.open("https://rahulshettyacademy.com/AutomationPractice/")
        self.assert_text("Practice Page", "//body//h1")
        self.tearDown()

    def test_suggestion_class_example_2(self):
        self.open("https://rahulshettyacademy.com/AutomationPractice/")
        self.assert_element("//input[@id='autocomplete']")
        self.type("//input[@id='autocomplete']", "Me")
        self.sleep(2)
        self.click("//ul[@id='ui-id-1']//*[text()='Mexico']")
        self.sleep(5)
        self.tearDown()


    def test_dropdown_example_3(self):
        self.open("https://rahulshettyacademy.com/AutomationPractice/")
        self.click("//select[@id='dropdown-class-example']")
        self.click("//option[contains(text(),'Option2')]")
        self.click("//body")
        self.sleep(3)
        self.click("//select[@id='dropdown-class-example']")
        self.click("//option[contains(text(),'Option3')]")
        self.click("//body")
        self.sleep(5)
