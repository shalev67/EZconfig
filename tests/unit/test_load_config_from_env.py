import os


class TestLoadConfigFromEnv:
    def test_load_config_from_env(self, config):
        config.register_config(name='test1', config_type=str, default='test1', env_var='TEST1')
        config.load_config_from_env()
        assert config.test1 == 'test1'
        os.environ['TEST1'] = 'test2'
        config.load_config_from_env()
        assert config.test1 == 'test2'
        del os.environ['TEST1']
        config.set_config('test1', 'test1')
        config.load_config_from_env()
        assert config.test1 == 'test1'

    def test_load_config_from_env_without_env_var(self, config):
        config.register_config(name='test1', config_type=str, default='test1')
        os.environ['TEST1'] = 'test2'
        config.load_config_from_env()
        assert config.test1 == 'test1'

    def test_load_config_from_env_str(self, config):
        config.register_config(name='test1', config_type=str, default='test1', env_var='TEST1')
        os.environ['TEST1'] = 'test2'
        config.load_config_from_env()
        assert config.test1 == 'test2'
        del os.environ['TEST1']

    def test_load_config_from_env_int(self, config):
        config.register_config(name='test1', config_type=int, default=1, env_var='TEST1')
        os.environ['TEST1'] = '3'
        config.load_config_from_env()
        assert config.test1 == 3
        del os.environ['TEST1']

    def test_load_config_from_env_float(self, config):
        config.register_config(name='test1', config_type=float, default=1.0, env_var='TEST1')
        os.environ['TEST1'] = '2.2'
        config.load_config_from_env()
        assert config.test1 == 2.2
        del os.environ['TEST1']

    def test_load_config_from_env_dict(self, config):
        config.register_config(name='test1', config_type=dict, default={}, env_var='TEST1')
        os.environ['TEST1'] = '{"a": 1, "b": "test1"}'
        config.load_config_from_env()
        assert type(config.test1) is dict
        del os.environ['TEST1']

    def test_load_config_from_env_list(self, config):
        config.register_config(name='test1', config_type=list, default=[], env_var='TEST1')
        os.environ['TEST1'] = '["1", 2, {}]'
        config.load_config_from_env()
        assert type(config.test1) is list
        del os.environ['TEST1']

    def test_load_config_from_env_bool(self, config):
        config.register_config(name='test1', config_type=bool, default=True, env_var='TEST1')
        os.environ['TEST1'] = 'FALSE'
        config.load_config_from_env()
        assert type(config.test1) is bool and not config.test1
        del os.environ['TEST1']

        os.environ['TEST1'] = 'False'
        config.load_config_from_env()
        assert type(config.test1) is bool and not config.test1
        del os.environ['TEST1']
