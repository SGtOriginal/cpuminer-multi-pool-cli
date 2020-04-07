from mining.pool.config.pool_config import PoolConfiguration
from mining.pool.config.pool_config_resolver import PoolConfigurationResolver
from mining.pool.config.pool_selection_info import PoolSelectionInfo
from mining.pool.config.pool_user_config import PoolUserConfiguration
from mining.pool.config.pool_user_config_resolver import PoolUserConfigurationResolver


class PoolSelector:

    def __init__(self,
                 pool_config_resolver: PoolConfigurationResolver,
                 pool_user_config_resolver: PoolUserConfigurationResolver):
        self.pool_config_resolver = pool_config_resolver
        self.pool_user_config_resolver = pool_user_config_resolver

    def select_pool(self, info: PoolSelectionInfo) -> (PoolConfiguration, PoolUserConfiguration):
        pool_configs = self.pool_config_resolver.resolve_all()
        pool_config_candidates = list(filter(info.matches_pool_configuration, pool_configs))
        if len(pool_config_candidates) > 0:
            pool_config = pool_config_candidates[0]
            pool_user_configs = self.pool_user_config_resolver.resolve_all()
            pool_user_config_candidates = list(filter(info.matches_pool_user_configuration, pool_user_configs))
            if len(pool_user_config_candidates) > 0:
                pool_user_config = pool_user_config_candidates[0]
                return pool_config, pool_user_config
        return None
