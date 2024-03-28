# -*- coding: utf-8 -*-
# @Author  : chenghua.yuan

import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    btn_more_section = (By.LINK_TEXT, "更多")

    def go_home_page(self):
        BasePage.goto_website(self, "")

    def goto_more_page(self):
        logger.info(f"Goto '更多' search page.")
        self.wait_for_element_clickable(*self.btn_more_section)
        self.click(*self.btn_more_section)
