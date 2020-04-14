import unittest

from mining.pool.config.pool_config import PoolConfiguration
from mining.pool.config.pool_config_resolver import BufferPoolConfigurationResolver
from mining.pool.config.pool_selection_info import PoolSelectionInfo
from mining.pool.config.pool_selector import PoolSelector
from mining.pool.config.pool_user_config import PoolUserConfiguration
from mining.pool.config.pool_user_config_resolver import BufferPoolUserConfigurationResolver


class PoolSelectorTestCase(unittest.TestCase):

    def test_no_pool_config_and_no_pool_user_config(self):
        pool_config_resolver = BufferPoolConfigurationResolver([])
        pool_user_config_resolver = BufferPoolUserConfigurationResolver([])
        pool_selector = PoolSelector(pool_config_resolver, pool_user_config_resolver)

        pool_selection_info = PoolSelectionInfo('pool1', 'currency1', 'algo1')

        configs = pool_selector.select_pool(pool_selection_info)

        self.assertIsNone(configs)

    def test_pool_config_and_no_pool_user_config(self):
        pool_config_resolver = BufferPoolConfigurationResolver([
            PoolConfiguration('pool1', [])
        ])
        pool_user_config_resolver = BufferPoolUserConfigurationResolver([])
        pool_selector = PoolSelector(pool_config_resolver, pool_user_config_resolver)

        pool_selection_info = PoolSelectionInfo('pool1', 'currency1', 'algo1')

        configs = pool_selector.select_pool(pool_selection_info)

        self.assertIsNone(configs)

    def test_no_pool_config_and_pool_user_config(self):
        pool_config_resolver = BufferPoolConfigurationResolver([])
        pool_user_config_resolver = BufferPoolUserConfigurationResolver([
            PoolUserConfiguration('pool1', 'user1', 'pass1')
        ])
        pool_selector = PoolSelector(pool_config_resolver, pool_user_config_resolver)

        pool_selection_info = PoolSelectionInfo('pool1', 'currency1', 'algo1')

        configs = pool_selector.select_pool(pool_selection_info)

        self.assertIsNone(configs)
    
    def test_matches_pool_config_and_matches_pool_user_config(self):
        pool_config_resolver = BufferPoolConfigurationResolver([
            PoolConfiguration('pool1', [])
        ])
        pool_user_config_resolver = BufferPoolUserConfigurationResolver([
            PoolUserConfiguration('pool1', 'user1', 'pass1')
        ])
        pool_selector = PoolSelector(pool_config_resolver, pool_user_config_resolver)

        pool_selection_info = PoolSelectionInfo('pool1', 'currency1', 'algo1')

        configs = pool_selector.select_pool(pool_selection_info)

        self.assertIsNotNone(configs)

        pool_config, pool_user_config = configs

        self.assertEqual('pool1', pool_config.pool_name)
        self.assertEqual('pool1', pool_user_config.pool_name)

    def test_matches_pool_config_and_matches_not_pool_user_config(self):
        pool_config_resolver = BufferPoolConfigurationResolver([
            PoolConfiguration('pool1', [])
        ])
        pool_user_config_resolver = BufferPoolUserConfigurationResolver([
            PoolUserConfiguration('pool2', 'user1', 'pass1')
        ])
        pool_selector = PoolSelector(pool_config_resolver, pool_user_config_resolver)

        pool_selection_info = PoolSelectionInfo('pool1', 'currency1', 'algo1')

        configs = pool_selector.select_pool(pool_selection_info)

        self.assertIsNone(configs)

    def test_matches_not_pool_config_and_matches_pool_user_config(self):
        pool_config_resolver = BufferPoolConfigurationResolver([
            PoolConfiguration('pool2', [])
        ])
        pool_user_config_resolver = BufferPoolUserConfigurationResolver([
            PoolUserConfiguration('pool1', 'user1', 'pass1')
        ])
        pool_selector = PoolSelector(pool_config_resolver, pool_user_config_resolver)

        pool_selection_info = PoolSelectionInfo('pool1', 'currency1', 'algo1')

        configs = pool_selector.select_pool(pool_selection_info)

        self.assertIsNone(configs)


if __name__ == '__main__':
    unittest.main()
