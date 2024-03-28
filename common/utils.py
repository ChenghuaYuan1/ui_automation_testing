# -*- coding: utf-8 -*-
# @Author  : chenghua.yuan
import logging
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as ff_Options
from selenium.webdriver.firefox.service import Service as ff_Service
from common.project import BROWSER_SETTING
import cv2

logger = logging.getLogger(__name__)


def get_driver():
    logger.info(f"Browser settings: {BROWSER_SETTING}")
    browser_type = BROWSER_SETTING.get("type", "Chrome")
    binary_path = BROWSER_SETTING.get("binary_path")
    driver_path = BROWSER_SETTING.get("driver_path")
    if browser_type == "Firefox":
        cls = webdriver.Firefox
    elif browser_type == "Chrome":
        cls = webdriver.Chrome
    else:
        raise ValueError(f"Unsupported Browser type '{browser_type}'")
    options, service = None, None
    if binary_path is not None:
        options = ff_Options() if browser_type == "Firefox" else Options()
        options.binary_location = binary_path
    if driver_path is not None:
        if browser_type == "Firefox":
            service = ff_Service(executable_path=driver_path)
        else:
            service = Service(executable_path=driver_path)
    driver = cls(options=options, service=service)
    driver.maximize_window()
    driver.implicitly_wait(3)
    return driver


def save_image_file(image_url, save_file_path):
    r = requests.get(image_url)
    logger.info(f"save image file to {save_file_path}")
    with open(save_file_path, 'wb') as f:
        f.write(r.content)


def compare_images_with_cv(image_path1, image_path2):
    image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)
    orb = cv2.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(image1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(image2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)
    similarity_score = len(matches) / len(keypoints1) * 100
    logger.debug(f"similarity_score is {similarity_score}")
    return similarity_score
