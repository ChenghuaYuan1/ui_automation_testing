# -*- coding: utf-8 -*-
# @Author  : chenghua.yuan

import logging
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
logger = logging.getLogger(__name__)


class SearchByImage(BasePage):
    main_window = (By.XPATH, "//div[@id='app']")
    upload_button = (By.XPATH, "//span[@class='graph-d20-search-wrapper-camera']")

    def wait_for_page_loaded(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        current_url = self.driver.current_url
        logger.debug(f"Current url is {current_url}")
        self.wait_element(*self.main_window)

    def upload_image(self, image_file):
        logger.info(f"Upload image {image_file} for searching.")
        self.wait_element(*self.upload_button)
        self.wait_for_element_clickable(*self.upload_button)
        self.click(*self.upload_button)
        hidden_input = self.driver.find_element(By.XPATH, "//input[@name='file']")
        hidden_input.send_keys(image_file)
        self.wait_for_page_loaded()