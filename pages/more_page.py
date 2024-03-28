# -*- coding: utf-8 -*-
# @Author  : chenghua.yuan

import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
logger = logging.getLogger(__name__)


class MorePage(BasePage):
    main_option_window = (By.XPATH, "//div[@id='content']")
    btn_search_by_image_section = (By.LINK_TEXT, "百度识图")

    def wait_for_page_loaded(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        current_url = self.driver.current_url
        logger.debug(f"Current url is {current_url}")
        self.wait_element(*self.main_option_window)

    def goto_search_by_image_page(self):
        logger.debug(f"Goto '百度识图' search page.")
        self.wait_element(*self.btn_search_by_image_section)
        self.wait_for_element_clickable(*self.btn_search_by_image_section)
        self.click(*self.btn_search_by_image_section)
        logger.debug(f"Click '百度识图' button.")