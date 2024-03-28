# -*- coding: utf-8 -*-
# @Author  : chenghua.yuan
import logging
import unittest
from common.utils import get_driver, compare_images_with_cv, save_image_file
from common.project import get_absolute_path, RESULT_IMAGE_FILE_FOLDER, ORIGINAL_IMAGE_FILE_FOLDER
from pages.home_page import HomePage
from pages.more_page import MorePage
from pages.search_by_image.search_by_image_page import SearchByImage
from pages.search_by_image.search_result_page import SearchByImageResult
from tests.image_search.custom_data import td
logger = logging.getLogger(__name__)


class TestSearchImage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        logger.info(f"Class '{cls.__name__}' set up".center(80, "-"))
        cls.driver = get_driver()
        HomePage(cls.driver).go_home_page()
        HomePage(cls.driver).goto_more_page()

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info(f"Class '{cls.__name__}' tear down".center(80, "-"))
        if cls.driver is not None:
            logger.info("Web driver quit.")
            cls.driver.quit()

    def setUp(self) -> None:
        logging.info(f"Start testing case ‘{self._testMethodName}’".center(80, "-"))

    def test_search_image(self):
        logger.info(f"Step1.Navigate to ‘百度识图’ page.".center(80, "-"))
        more_page = MorePage(self.driver)
        more_page.wait_for_page_loaded()
        more_page.goto_search_by_image_page()

        logger.info(f"Step2.Upload the original image to search.".center(80, "-"))
        search_by_image_page = SearchByImage(self.driver)
        search_by_image_page.wait_for_page_loaded()
        image_path = get_absolute_path(ORIGINAL_IMAGE_FILE_FOLDER, td.original_image)
        search_by_image_page.upload_image(image_path)

        logger.info(f"Step3.Choose the specific result image to download.".center(80, "-"))
        search_by_image_result = SearchByImageResult(self.driver)
        image_url = search_by_image_result.get_image_url(td.visit_result)
        self.assertTrue(image_url, f"There is no image with the specific number {td.visit_result}")
        save_file_path = get_absolute_path(RESULT_IMAGE_FILE_FOLDER, td.result_image)
        save_image_file(image_url, save_file_path)

        logger.info(f"Step4.Compare the original image and the specific result image.".center(80, "-"))
        similarity_score = compare_images_with_cv(image_path, save_file_path)
        logger.info(f"Images similarity_score is {similarity_score}.")
        self.assertTrue(similarity_score > td.similarity_score, f"The search result image is not related to the used "
                                                                f"image.")

    def tearDown(self) -> None:
        logger.info(f"Test case '{self._testMethodName}' tear down.".center(80, "-"))