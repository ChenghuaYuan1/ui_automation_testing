# -*- coding: utf-8 -*-
# @Author  : chenghua.yuan

import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.project import get_absolute_path
from pages.base_page import BasePage
from pages.home_page import HomePage
from selenium.webdriver.common.keys import Keys

logger = logging.getLogger(__name__)


class SearchByImageResult(BasePage):
    # image_list = (By.XPATH, "//div[@class='graph-same-list-item']//img")
    image_list = (By.XPATH, "//a[@class='general-imgcol-item']//img")
    image = (By.XPATH, "//img")

    def get_search_results(self):
        results = self.find_elements(*self.image_list)
        return results

    def get_search_result(self, index):
        results = self.get_search_results()
        logger.info(f"There are {len(results)} result items")
        if len(results) >= index:
            for i, item in enumerate(results):
                if i + 1 == index:
                    return item
        return None

    def get_image_url(self, index):
        logger.info(f"The index is {index}")
        download_image = self.get_search_result(index)
        if not download_image:
            return None
        src_url = download_image.get_attribute("src")
        return src_url

    # def download_image(self, index):
    #     download_image = self.get_search_result(index)
    #     src_url = download_image.get_attribute("src")
    #     self.goto_website(src_url)
    #     image = self.find_element(*self.image)
    #     action = webdriver.ActionChains(self.driver).move_to_element(image)
    #     action.context_click(image).perform()
    #     action.send_keys(Keys.ARROW_DOWN).perform()
    #     action.send_keys('v').perform()
    #     action.perform()
    #     print(f"Finish downloading the image")
    # action = ActionChains(self.driver).move_to_element(download_image)
