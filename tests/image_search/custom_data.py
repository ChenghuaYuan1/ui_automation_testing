# -*- coding: utf-8 -*-
# @Author  : chenghua.yuan

import os
import yaml
from common.project import get_absolute_path

data_file = get_absolute_path(os.path.dirname(__file__), "data.yaml")


class TestData(object):
    def __init__(self):
        with open(data_file) as f:
            data = yaml.safe_load(f)
            self.original_image = data["image"]["file_name"]
            self.result_image = data["image"]["result_file_name"]
            self.visit_result = data["image"]["visit_result"]
            self.similarity_score = data["image"]["similarity_score"]


td = TestData()
