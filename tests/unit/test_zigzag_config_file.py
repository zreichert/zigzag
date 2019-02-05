# -*- coding: utf-8 -*-

# ======================================================================================================================
# Imports
# ======================================================================================================================
import pytest
from zigzag.zigzag_config import ZigZagConfig
from zigzag.zigzag_error import ZigZagConfigError

# ======================================================================================================================
# Fixtures
# ======================================================================================================================
@pytest.fixture(scope='session')
def config_with_interpolation(tmpdir_factory):
    """config with one value in a jinga template"""
    config = \
        """
        {
            "test_cycle": "pike",
            "project_id": 12345,
            "module_hierarchy": ["one","two","three"],
            "path_to_test_exec_dir": "{{ FOO }}"
        }
        """ # noqa

    config_path = tmpdir_factory.mktemp('data').join('./conf.json').strpath

    with open(str(config_path), 'w') as f:
        f.write(config)

    return config_path


# ======================================================================================================================
# Test Suites
# ======================================================================================================================
class TestZigZagConfig(object):
    """Test cases for ZigZagConfig"""

    def test_pull_value_from_properties(self, config_with_interpolation):
        """Test that we can interpolate one value successfully"""

        properties = {'FOO': '/Hello/is/it/me/youre/looking/for'}
        config = ZigZagConfig(config_with_interpolation, properties)
        assert properties['FOO'] == config['path_to_test_exec_dir']

    def test_access_config_not_present(self, config_with_interpolation):
        """Test that we will raise error if value defined in config
        is not present in the global properties"""

        properties = {}
        config = ZigZagConfig(config_with_interpolation, properties)
        expected_message = "The config 'path_to_test_exec_dir' was not found in the config file"

        with pytest.raises(ZigZagConfigError, match=expected_message):
            config['path_to_test_exec_dir']

    def test_config_not_json(self, invalid_zigzag_config_file):
        """Test that we will raise error if value defined in config
        is not present in the global properties"""

        properties = {}
        expected_message = 'config file is not valid JSON'
        with pytest.raises(ZigZagConfigError, match=expected_message):
            ZigZagConfig(invalid_zigzag_config_file, properties)