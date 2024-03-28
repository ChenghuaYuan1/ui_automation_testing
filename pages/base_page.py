# -*- coding: utf-8 -*-
# @Author  : chenghua.yuan

import time
import logging
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.project import BASE_URL

logger = logging.getLogger(__name__)


class BasePage(object):
    is_operator = None

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        logger.debug(f"Find element with locator '{loc}'")
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        logger.debug(f"Find elements with locator '{loc}'")
        return self.driver.find_elements(*loc)

    def input(self, *loc, value, clear_first=False):
        if value is None:
            return
        ele = self.find_element(*loc)
        try:
            if clear_first:
                ele.clear()
            ele.send_keys(value)
        except ElementNotInteractableException:
            time.sleep(0.5)
            if clear_first:
                ele.clear()
            ele.send_keys(value)
        # Find next element failed if value is longer than displayed area.
        # simulator "Tab" to change focus to avoid the issue.
        ele.send_keys(Keys.TAB)

    def click(self, *loc, element=None):
        """
        click an element specified by locator or object.
        :param loc: element locator for 'click' operation.
        :param element: element for 'click' operation.
        :return:
        """

        def try_to_click(ele):
            try:
                ele.click()
            except ElementClickInterceptedException:
                webdriver.ActionChains(self.driver).move_to_element(ele).click(ele).perform()

        if element is None:
            if not loc:
                raise ValueError("Element or locator is required for 'click' operation.")
            element = self.find_element(*loc)
        try:
            try_to_click(element)
        except ElementNotInteractableException:
            time.sleep(0.5)
            try_to_click(element)

    def wait_element(self, *loc, timeout=15, interval=0.5):
        logger.debug(f"Wait for element with locator {loc} present.")
        WebDriverWait(self.driver, timeout=timeout, poll_frequency=interval).until(EC.presence_of_element_located(loc))

    def wait_for_element_clickable(self, *loc, timeout=15, interval=0.5):
        logger.debug(f"Wait for element with locator {loc} to be clickable.")
        WebDriverWait(self.driver, timeout=timeout, poll_frequency=interval).until(EC.element_to_be_clickable(loc))

    def goto_website(self, url):
        url = url if url.startswith("http") else urljoin(BASE_URL, url)
        logger.debug(f"Go to URL '{url}'")
        if self.driver.current_url != url:
            self.driver.get(url)

    def _goto_home_page(self):
        self.goto_website()
