import unittest
from pathlib import Path
from utils.load_config import _parse_config, _validate_config
from utils.load_config import UnsetConfigValueException
from utils.path import get_project_dir, here
from yaml.scanner import ScannerError


class TestConfigValidation(unittest.TestCase):

    @staticmethod
    def built_test_config_path(config_name):
        return Path(__file__).parent.joinpath("testdata").joinpath("".join([config_name, ".yml"]))

    def test_parse_config_given_invalid_path(self):
        invalid_conf_path = TestConfigValidation.built_test_config_path("invalid.yml")
        self.assertRaises(FileNotFoundError, _parse_config, invalid_conf_path, "dev")

    def test_parse_inparsable_config(self):
        path_to_inparsable_conf = TestConfigValidation.built_test_config_path("inparsable_config")
        c = _parse_config(path_to_inparsable_conf, "dev")
        self.assertIs(c, None)

    def test_parse_invalid_config(self):
        path_to_invalid_conf = TestConfigValidation.built_test_config_path("invalid_config")
        cfg = _parse_config(path_to_invalid_conf, "tst")
        self.assertIs(type(cfg), dict)

    def test_parse_valid_config(self):
        path_to_invalid_conf = TestConfigValidation.built_test_config_path("valid_config")
        cfg = _parse_config(path_to_invalid_conf, "tst")
        self.assertIs(type(cfg), dict)

    def test_validate_invalid_conf(self):
        path_to_invalid_conf = TestConfigValidation.built_test_config_path("invalid_config")
        cfg = _parse_config(path_to_invalid_conf, "tst")
        self.assertRaises(UnsetConfigValueException, _validate_config, cfg, "tst")

    def test_validate_valid_conf(self):
        path_to_valid_conf = TestConfigValidation.built_test_config_path("valid_config")
        cfg = _parse_config(path_to_valid_conf, "dev")
        self.assertTrue(_validate_config(cfg, "dev"))


class TestRelativePathBuilding(unittest.TestCase):
    def test_here_given_list(self):
        self.assertEqual(
            here(["relative", "sub", "dir"], Path(__file__).parent),
            Path(__file__).parent.joinpath("relative").joinpath("sub").joinpath("dir"))

    def test_here_given_str(self):
        self.assertEqual(
            here("relative/sub/dir", Path(__file__).parent),
            Path(__file__).parent.joinpath("relative").joinpath("sub").joinpath("dir"))