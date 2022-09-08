from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from data import data as config


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_presents(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_elements(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();^element")

    def clear_inputbox(self, element):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def change_tab(self, driver, id):
        driver.switch_to.window(driver.window_handles[id])

    def refresh(self, driver):
        driver.refresh()
