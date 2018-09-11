import pytest


class TestBasicConfig:
    def test_register_config(self, config):
        config.register_config(name='test1', config_type=str, default='test1')
        assert config.test1 == 'test1'

    def test_unregister_config(self, config):
        config.register_config(name='test1', config_type=str, default='test1')
        config.unregister_config('test1')
        with pytest.raises(AttributeError):
            assert config.test1

    def test_list_config(self, config):
        config.register_config(name='test1', config_type=str, default='test1')
        config.register_config(name='test2', config_type=str, default='test2')
        config.register_config(name='test3', config_type=str, default='test3')
        assert set(config.list_config()) == {'test1', 'test2', 'test3'}
        config.unregister_config(name='test1')
        config.unregister_config(name='test3')
        assert config.list_config() == ['test2']

    def test_get_config(self, config):
        config.register_config(name='test1', config_type=str, default='test1')
        test_get = config.get_config('test1')
        assert type(test_get) is dict

    def test_register_config_bad_config_type(self, config):
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type='test1', default='test1')

    def test_reregister_config(self, config):
        config.register_config(name='test1', config_type=str, default='test1')
        assert config.test1 == 'test1'
        config.register_config(name='test1', config_type=int, default=1)
        assert config.test1 == 1
        config.register_config(name='test1', config_type=float, default=1.2)
        assert config.test1 == 1.2
        config.register_config(name='test1', config_type=dict, default={})
        assert config.test1 == {}
        config.register_config(name='test1', config_type=list, default=[])
        assert config.test1 == []
        config.register_config(name='test1', config_type=bool, default=False)
        assert type(config.test1) is bool and not config.test1

    def test_register_config_bad_default_value_type(self, config):
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=int, default='test1')
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=str, default=1)
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=float, default='test1')
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=str, default=1.2)
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=dict, default='test1')
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=dict, default=[])
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=list, default='test1')
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=bool, default='false')

    def test_register_config_bad_value_type(self, config):
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=int, default=1, value='test1')
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=str, default='test1', value=1)
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=float, default=1.2, value='test1')
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=str, default='test1', value=1)
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=dict, default={}, value='test1')
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=dict, default={}, value=[])
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=list, default=[], value=1)
        with pytest.raises(TypeError):
            config.register_config(name='test1', config_type=bool, default=True, value=1)
