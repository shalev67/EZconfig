import os
import pytest


class TestLoadConfigFromJson:
    def test_load_config_from_json(self, config):
        config.register_config(name='a', config_type=str, default='test1')
        config.register_config(name='b', config_type=int, default=0)
        config.register_config(name='c', config_type=float, default=0.0)
        config.register_config(name='d', config_type=list, default=[])
        config.register_config(name='e', config_type=dict, default={})
        config.register_config(name='f', config_type=bool, default=False)
        config.register_config(name='g', config_type=bool, default=True)
        dir_name = os.path.dirname(os.path.abspath(__file__))
        config.load_config_from_json_file(dir_name + '/config_files/json_config.json')
        assert config.a == 'a'
        assert config.b == 1
        assert config.c == 1.2
        assert config.d == [1, 2, 3]
        assert config.e == {"1": 1}
        assert type(config.f) is bool and config.f
        assert type(config.g) is bool and not config.g
        with pytest.raises(AttributeError):
            assert config.h
