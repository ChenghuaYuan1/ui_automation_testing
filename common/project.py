# -*- coding: utf-8 -*-
# @Author  : chenghua.yuan
import os
import yaml
import logging.config
from copy import deepcopy

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def get_absolute_path(*relative_path):
    # Get absolute path in local.
    cur_sep = os.path.sep
    other_sep = "/" if cur_sep != "/" else "\\"
    correct_paths = []
    for path in [BASE_DIR] + list(relative_path):
        if path.find(other_sep) != -1:
            path = path.replace(other_sep, cur_sep)
        if path.endswith(":"):
            path = path + os.path.sep
        correct_paths.append(path.lstrip("\\"))
    return os.path.join(*correct_paths)


def _get_all_settings(setting_file="settings/config.yaml"):
    setting_file = get_absolute_path(setting_file)
    with open(setting_file, encoding="utf-8") as f:
        config = yaml.safe_load(f.read())
    return config


_SETTINGS = _get_all_settings()


def _get_settings(*keys):
    config = deepcopy(_SETTINGS)
    for key in keys:
        config = config[key]
    return config


def init_log_setting():
    log_folder = get_absolute_path(BASE_DIR, _get_settings("log_folder"))
    os.makedirs(log_folder, exist_ok=True)

    log_config_file = get_absolute_path(BASE_DIR, _get_settings("log_config"))
    with open(log_config_file) as f:
        log_config = yaml.safe_load(f.read())
        for handler, config in log_config["handlers"].items():
            if config["formatter"] == "file":
                config["filename"] = get_absolute_path(log_folder, config["filename"])
    logging.config.dictConfig(log_config)


__base_url = _get_settings("base_url")
BASE_URL = __base_url if __base_url.endswith("/") else __base_url + "/"
BROWSER_SETTING = _get_settings("browser")
REPORT_FILE = get_absolute_path(BASE_DIR, _get_settings("report_file"))
ORIGINAL_IMAGE_FILE_FOLDER = get_absolute_path(BASE_DIR, _get_settings("original_image_file"))
RESULT_IMAGE_FILE_FOLDER = get_absolute_path(BASE_DIR, _get_settings("result_image_file"))
