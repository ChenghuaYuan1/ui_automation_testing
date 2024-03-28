# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
import os
import unittest
from common.HTMLTestRunner import HTMLTestRunner as Runner
from common.project import REPORT_FILE
from tests.image_search.test_search_image import TestSearchImage

if __name__ == '__main__':
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(
        [
            TestSearchImage("test_search_image"),
        ]
    )

    with open(REPORT_FILE, "wb") as fp:      # Run cases and save result to report file
        runner = Runner(stream=fp, title="test_report")
        result = runner.run(suite)
